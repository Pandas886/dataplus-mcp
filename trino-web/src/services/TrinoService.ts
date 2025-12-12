import axios from 'axios';

export interface TrinoResult {
    id: string;
    columns?: Array<{ name: string; type: string }>;
    data?: any[][];
    error?: any;
    nextUri?: string;
    stats?: any;
}

export interface QueryResult {
    id: string;
    columns: Array<{ name: string; type: string }>;
    rows: any[][];
}

export class TrinoService {

    // Submit query and follow paging to get full results
    static async execute(sql: string, catalog?: string, schema?: string): Promise<QueryResult> {
        // Initial request
        const headers: any = {
            'X-Trino-User': 'admin'
        }
        if (catalog) headers['X-Trino-Catalog'] = catalog
        if (schema) headers['X-Trino-Schema'] = schema

        let response = await axios.post<TrinoResult>('/v1/statement', sql, {
            headers
        });

        let result = response.data;

        const finalColumns: Array<{ name: string; type: string }> = [];
        const finalRows: any[][] = [];
        const queryId = result.id;

        // Loop until finished
        while (result.nextUri || result.data) {

            if (result.error) {
                throw new Error(result.error.message);
            }

            if (result.columns && finalColumns.length === 0) {
                finalColumns.push(...result.columns);
            }

            if (result.data) {
                finalRows.push(...result.data);
            }

            if (!result.nextUri) {
                break;
            }

            // Fix: Trino returns absolute URLs (http://localhost:8080/...) which bypass our proxy
            // We need to make them relative to go through Vite proxy
            const nextLink = result.nextUri.replace(/^https?:\/\/[^\/]+/, '');

            // Fetch next page
            response = await axios.get<TrinoResult>(nextLink);
            result = response.data;
        }

        if (result.error) {
            throw new Error(result.error.message);
        }

        return {
            id: queryId,
            columns: finalColumns,
            rows: finalRows
        };
    }

    static async getCatalogs(): Promise<{ name: string, connector: string }[]> {
        try {
            const res = await this.execute('SELECT catalog_name, connector_id FROM system.metadata.catalogs ORDER BY catalog_name');
            return res.rows.map(r => ({ name: r[0], connector: r[1] }));
        } catch (e) {
            // Fallback if system catalog is not accessible
            const res = await this.execute('SHOW CATALOGS');
            return res.rows.map(r => ({ name: r[0], connector: 'unknown' }));
        }
    }

    static async getSchemas(catalog: string): Promise<string[]> {
        const res = await this.execute(`SHOW SCHEMAS FROM "${catalog}"`);
        return res.rows.map(r => r[0]);
    }

    static async getTables(catalog: string, schema: string): Promise<string[]> {
        const res = await this.execute(`SHOW TABLES FROM "${catalog}"."${schema}"`);
        return res.rows.map(r => r[0]);
    }
}
