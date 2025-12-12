<template>
  <div class="catalog-tree-container">
    <div class="header">
        <div class="title-row">
            <span>Data Explorer</span>
            <div class="actions">
                <el-button link type="primary" @click="refresh" title="Refresh">
                    <el-icon><Refresh /></el-icon>
                </el-button>
                <el-button link type="primary" @click="showAddCatalog = true" title="Add Catalog">
                    <el-icon><Plus /></el-icon>
                </el-button>
            </div>
        </div>
        <div class="search-box">
            <el-input v-model="filterText" placeholder="Search" :prefix-icon="Search" clearable />
        </div>
    </div>

    <el-tree
        ref="treeRef"
        :key="treeKey"
        :props="props"
        :load="loadNode"
        lazy
        @node-click="handleNodeClick"
        highlight-current
        class="custom-tree"
        :filter-node-method="filterNode"
     >
      <template #default="{ node, data }">
        <span class="custom-tree-node">
          <!-- Catalog Icon Logic -->
          <el-icon v-if="node.level === 1" class="icon-blue">
            <component :is="getCatalogIcon(data)" />
          </el-icon>
          <el-icon v-else-if="node.level === 2" class="icon-yellow"><Folder /></el-icon>
          <el-icon v-else><Document /></el-icon>
          
          <span class="node-label">{{ node.label }}</span>
          
          <!-- Delete Catalog Button (only on hover for catalogs) -->
          <span v-if="node.level === 1" class="actions" @click.stop="deleteCatalog(data.name)">
             <el-icon class="delete-icon"><Delete /></el-icon>
          </span>
        </span>
      </template>
    </el-tree>

    <!-- Add Catalog Dialog -->
    <el-dialog v-model="showAddCatalog" title="Add Catalog" width="500px">
        <el-form :model="newCatalog" label-width="100px">
            <el-form-item label="Name">
                <el-input v-model="newCatalog.name" placeholder="my_catalog" />
            </el-form-item>
            <el-form-item label="Connector">
                <el-select v-model="newCatalog.connector" placeholder="Select connector" filterable allow-create>
                    <el-option label="tpch" value="tpch" />
                    <el-option label="tpcds" value="tpcds" />
                    <el-option label="memory" value="memory" />
                    <el-option label="hive" value="hive" />
                    <el-option label="postgresql" value="postgresql" />
                    <el-option label="mysql" value="mysql" />
                    <el-option label="system" value="system" />
                    <!-- Add more as needed -->
                </el-select>
            </el-form-item>
            
            <el-divider content-position="left">Properties</el-divider>
            
            <div v-for="(prop, index) in newCatalog.properties" :key="index" class="property-row">
                <el-input v-model="prop.key" placeholder="Key" style="width: 140px" />
                <span class="eq">=</span>
                <el-input v-model="prop.value" placeholder="Value" style="width: 140px" />
                <el-button type="danger" link @click="removeProperty(index)"><el-icon><Delete /></el-icon></el-button>
            </div>
            <el-button type="primary" link @click="addProperty">+ Add Property</el-button>
        </el-form>
        <template #footer>
            <span class="dialog-footer">
                <el-button @click="showAddCatalog = false">Cancel</el-button>
                <el-button type="primary" @click="handleCreateCatalog" :loading="creating">Create</el-button>
            </span>
        </template>
    </el-dialog>
  </div>
</template>

<script setup lang="ts">
import { ref, watch } from 'vue'
import { Folder, Document, Plus, Delete, Search, DataBoard, Coin, Setting, Refresh, Odometer, Box, Connection } from '@element-plus/icons-vue'
import { TrinoService } from '../services/TrinoService'
import { ElMessage, ElMessageBox } from 'element-plus'

const emit = defineEmits(['node-click'])
const filterText = ref('')
const treeRef = ref()
const showAddCatalog = ref(false)
const creating = ref(false)
const treeKey = ref(0)

const newCatalog = ref({
    name: '',
    connector: '',
    properties: [] as {key: string, value: string}[]
})

watch(() => newCatalog.value.connector, (val) => {
    let props: {key: string, value: string}[] = []
    switch(val) {
        case 'tpch':
            props = [{ key: 'tpch.column-naming', value: 'SIMPLIFIED' }]
            break
        case 'tpcds':
            props = []
            break
        case 'memory':
            props = [{ key: 'max-data-per-node', value: '128MB' }]
            break
        case 'hive':
            props = [
                { key: 'hive.metastore.uri', value: 'thrift://localhost:9083' },
                { key: 'hive.config.resources', value: '' }
            ]
            break
        case 'postgresql':
        case 'mysql':
            props = [
                { key: 'connection-url', value: `jdbc:${val}://host:port/database` },
                { key: 'connection-user', value: 'root' },
                { key: 'connection-password', value: 'secret' }
            ]
            break
        case 'kafka':
             props = [
                { key: 'kafka.nodes', value: 'host:9092' },
                { key: 'kafka.table-names', value: 'table1,table2' },
                { key: 'kafka.hide-internal-columns', value: 'false' },
                { key: 'kafka.default-schema', value: 'default' }
            ]
            break
    }
    // Only set if properties are empty to avoid overwriting user input
    if (newCatalog.value.properties.length === 0 || (newCatalog.value.properties.length === 1 && !newCatalog.value.properties[0]?.key)) {
         newCatalog.value.properties = props
    }
})

const props = {
  label: 'name',
  children: 'zones',
  isLeaf: 'leaf',
}

watch(filterText, (val) => {
  treeRef.value!.filter(val)
})

const filterNode = (value: string, data: any) => {
  if (!value) return true
  return data.name.includes(value)
}

const getCatalogIcon = (data: any) => {
    // If we have connector info, use it
    if (data.connector) {
        if (data.connector.includes('system')) return Setting
        if (data.connector.includes('tpch') || data.connector.includes('tpcds')) return Coin
        if (data.connector.includes('memory')) return Odometer
        if (data.connector.includes('hive') || data.connector.includes('iceberg') || data.connector.includes('delta')) return Box
        if (data.connector.includes('sql') || data.connector.includes('jdbc')) return Connection
    }
    // Fallback/Legacy
    const name = data.name
    if (name === 'system') return Setting
    if (name.includes('tpch') || name.includes('tpcds')) return Coin
    return DataBoard
}

const loadNode = async (node: any, resolve: any) => {
  if (node.level === 0) {
    try {
        const catalogs = await TrinoService.getCatalogs()
        // Map API result to tree nodes
        return resolve(catalogs.map((c: any) => ({ 
            name: c.name, 
            connector: c.connector, 
            type: 'catalog' 
        })))
    } catch(e) {
        console.error(e)
        return resolve([])
    }
  }
  if (node.level === 1) {
    const catalog = node.data.name
    try {
        const schemas = await TrinoService.getSchemas(catalog)
        return resolve(schemas.map((s: string) => ({ name: s, type: 'schema', catalog })))
    } catch(e) {
        return resolve([])
    }
  }
  if (node.level === 2) {
    const catalog = node.data.catalog
    const schema = node.data.name
    try {
        const tables = await TrinoService.getTables(catalog, schema)
        return resolve(tables.map((t: string) => ({ 
            name: t, 
            type: 'table',
            catalog,
            schema,
            leaf: true
        })))
    } catch(e) {
        return resolve([])
    }
  }
  return resolve([])
}

const handleNodeClick = (data: any) => {
    emit('node-click', data)
}

const addProperty = () => {
    newCatalog.value.properties.push({ key: '', value: '' })
}

const removeProperty = (index: number) => {
    newCatalog.value.properties.splice(index, 1)
}

const handleCreateCatalog = async () => {
    if(!newCatalog.value.name || !newCatalog.value.connector) {
        ElMessage.error('Name and Connector are required')
        return
    }
    creating.value = true
    try {
        // Construct SQL
        // CREATE CATALOG <name> USING <connector> WITH (key=value, ...)
        let sql = `CREATE CATALOG "${newCatalog.value.name}" USING ${newCatalog.value.connector}`
        if (newCatalog.value.properties.length > 0) {
            const props = newCatalog.value.properties
                .filter(p => p.key && p.value)
                .map(p => `"${p.key}" = '${p.value}'`)
                .join(', ')
            if (props) {
                sql += ` WITH (${props})`
            }
        }
        await TrinoService.execute(sql)
        ElMessage.success('Catalog created')
        showAddCatalog.value = false
        // Refresh tree (reload root)
        refresh()
    } catch (e: any) {
        ElMessage.error('Failed to create catalog: ' + e.message)
    } finally {
        creating.value = false
    }
}

const deleteCatalog = (name: string) => {
    ElMessageBox.confirm(
        `Are you sure you want to drop catalog "${name}"?`,
        'Warning',
        {
          confirmButtonText: 'Yes',
          cancelButtonText: 'Cancel',
          type: 'warning',
        }
    ).then(async () => {
        try {
            await TrinoService.execute(`DROP CATALOG "${name}"`)
            ElMessage.success('Catalog deleted')
            refresh()
        } catch (e: any) {
             ElMessage.error('Failed to delete: ' + e.message)
        }
    })
}

const refresh = () => {
    // Increment key to force re-render of tree
    treeKey.value++
}
</script>

<style scoped>
.catalog-tree-container {
    height: 100%;
    display: flex;
    flex-direction: column;
    border-right: 1px solid #dcdfe6;
    background: #fff;
}
.header {
    padding: 10px;
    border-bottom: 1px solid #ebeef5;
    flex-shrink: 0;
}
.title-row {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 8px;
    font-weight: bold;
    color: #303133;
}
.search-box {
    margin-bottom: 5px;
}
.custom-tree {
    flex: 1;
    overflow: auto;
}
.custom-tree-node {
    display: flex;
    align-items: center;
    font-size: 13px;
    flex: 1;
    justify-content: space-between;
    padding-right: 8px; 
}
.node-label {
    margin-left: 6px;
    overflow: hidden;
    text-overflow: ellipsis;
    flex: 1;
}
.actions {
    display: none;
}
.custom-tree-node:hover .actions {
    display: inline-flex;
}
.delete-icon {
    color: #f56c6c;
    font-size: 12px;
}
.icon-blue { color: #409EFF; }
.icon-yellow { color: #E6A23C; }

.property-row {
    display: flex;
    align-items: center;
    gap: 5px;
    margin-bottom: 5px;
}
.eq { color: #909399; font-weight: bold; }
</style>
