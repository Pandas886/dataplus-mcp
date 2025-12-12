<template>
  <div class="results-container" v-loading="loading">
    <div v-if="error" class="error-msg">
        <el-alert title="Query Failed" type="error" :description="error" show-icon />
    </div>
    
    <div v-else-if="!data" class="empty-state">
        <el-empty description="No results" />
    </div>

    <div v-else class="table-wrapper">
        <div class="stats-bar">
            <span>Query ID: {{ data.id }}</span>
            <span style="margin-left: 20px">{{ data.rows.length }} rows</span>
        </div>
        <el-table :data="tableData" border style="width: 100%; height: 100%" height="100%">
            <el-table-column 
                v-for="col in columns"
                :key="col.name"
                :prop="col.name"
                :label="col.name"
                min-width="150"
                sortable
            >
                <template #default="scope">
                    <span :title="String(scope.row[col.name])" class="cell-content">
                        {{ scope.row[col.name] }}
                    </span>
                </template>
            </el-table-column>
        </el-table>
    </div>
  </div>
</template>

<script setup lang="ts">
import { computed } from 'vue'

const props = defineProps({
    data: {
        type: Object as () => { id: string, columns: any[], rows: any[][] } | null,
        default: null
    },
    loading: Boolean,
    error: String
})

const columns = computed(() => {
    if (!props.data || !props.data.columns) return []
    return props.data.columns
})

const tableData = computed(() => {
    if (!props.data || !props.data.rows) return []
    // Convert array of arrays to array of objects for el-table
    // el-table prefers objects keyed by prop
    return props.data.rows.map((row) => {
        const rowObj: any = {}
        props.data?.columns.forEach((col, idx) => {
            rowObj[col.name] = row[idx]
        })
        return rowObj
    })
})
</script>

<style scoped>
.results-container {
    height: 100%;
    display: flex;
    flex-direction: column;
    overflow: hidden;
    background: #fff;
    border-top: 1px solid #dcdfe6;
}
.error-msg, .empty-state {
    padding: 20px;
}
.table-wrapper {
    flex: 1;
    display: flex;
    flex-direction: column;
    overflow: hidden;
}
.stats-bar {
    padding: 8px 16px;
    background: #f8fafc;
    border-bottom: 1px solid var(--border-color);
    font-size: 13px;
    color: #64748b;
    font-weight: 500;
}
.cell-content {
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
    display: block;
}
</style>
