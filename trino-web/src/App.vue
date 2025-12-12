<template>
  <div class="main-layout">
    <splitpanes class="default-theme">
      <pane size="20" min-size="15">
        <CatalogTree @node-click="handleNodeClick" />
      </pane>
      <pane>
        <splitpanes horizontal>
          <pane size="60">
            <div class="editor-container">

               <!-- Toolbar -->
               <div class="toolbar">
                 <div class="left-tools">
                    <span class="context-label">Context:</span>
                    <el-input v-model="selectedCatalog" placeholder="Catalog" style="width: 140px" clearable />
                    <span class="context-sep">/</span>
                    <el-input v-model="selectedSchema" placeholder="Schema" style="width: 140px" clearable />
                 </div>
                 <div class="right-tools">
                    <el-button type="primary" class="run-btn" @click="runQuery" :loading="loading">
                        <el-icon><VideoPlay /></el-icon> Run Query
                    </el-button>
                 </div>
               </div>

               <SqlEditor v-model="currentSql" />
            </div>
          </pane>
          <pane size="40">
             <div class="bottom-panel">
                <el-tabs v-model="bottomTab" type="border-card" class="bottom-tabs">
                    <el-tab-pane label="Result Analysis" name="result">
                         <ResultsTable :data="queryResult" :loading="loading" :error="error" />
                    </el-tab-pane>
                    <el-tab-pane label="Run History" name="history">
                        <div class="history-mock">
                            <el-table :data="historyMock" style="width: 100%">
                                <el-table-column prop="status" label="Status" width="100">
                                    <template #default>
                                        <el-tag type="success">Success</el-tag>
                                    </template>
                                </el-table-column>
                                <el-table-column prop="time" label="Time" width="180" />
                                <el-table-column prop="duration" label="Duration" width="100" />
                                <el-table-column prop="sql" label="SQL" show-overflow-tooltip />
                            </el-table>
                        </div>
                    </el-tab-pane>
                </el-tabs>
             </div>
          </pane>
        </splitpanes>
      </pane>
    </splitpanes>
  </div>
</template>

<script setup lang="ts">
import { Splitpanes, Pane } from 'splitpanes'
import 'splitpanes/dist/splitpanes.css'
import { ref } from 'vue'
import { VideoPlay } from '@element-plus/icons-vue'
import CatalogTree from './components/CatalogTree.vue'
import SqlEditor from './components/SqlEditor.vue'
import ResultsTable from './components/ResultsTable.vue'
import { TrinoService } from './services/TrinoService'

const currentSql = ref('SELECT 1 as id, \'Hello Trino\' as msg')
const queryResult = ref<{ id: string; columns: any[], rows: any[][] } | null>(null)
const loading = ref(false)
const error = ref('')
const bottomTab = ref('result')
const historyMock = ref([
    { status: 'Success', time: '2024/10/29 17:30:32', duration: '12.4s', sql: 'select * from tpch.sf1.customer limit 100'}
])

const selectedCatalog = ref('')
const selectedSchema = ref('')

const handleNodeClick = (node: any) => {
  if (node.catalog) {
    selectedCatalog.value = node.catalog
  }
  if (node.schema) {
    selectedSchema.value = node.schema
  }
  
  if (node.type === 'table') {
    // Generate a select query for the table
    // If context matches, we can use simple names, but safe to use fully qualified for generated queries
    // or we can just use "SELECT * FROM name LIMIT 100" and rely on context.
    // The user requirement says "even if not entered catalog/schema should work".
    // For generated query, fully qualified is safer, but let's stick to what we had or maybe simplify if context is set?
    // Let's keep fully qualified for generated queries as they are unambiguous.
    currentSql.value = `SELECT * FROM "${node.catalog}"."${node.schema}"."${node.name}" LIMIT 100`
  }
}

const runQuery = async () => {
    loading.value = true
    error.value = ''
    queryResult.value = null
    bottomTab.value = 'result'
    try {
        const res = await TrinoService.execute(currentSql.value, selectedCatalog.value, selectedSchema.value)
        
        queryResult.value = {
            id: res.id,
            columns: res.columns, 
            rows: res.rows
        }
        // Add to history
        historyMock.value.unshift({
            status: 'Success',
            time: new Date().toLocaleString(),
            duration: '0.5s', // Mock
            sql: currentSql.value
        })
    } catch (e: any) {
        error.value = e.message || String(e)
    } finally {
        loading.value = false
    }
}
</script>

<style scoped>
.main-layout {
  height: 100vh;
  width: 100vw;
  display: flex;
  flex-direction: column;
  background: #fff;
}
.editor-container {
    height: 100%;
    display: flex;
    flex-direction: column;
}
.editor-tabs {
    display: flex;
    background: #f5f7fa;
    border-bottom: 1px solid #e4e7ed;
    padding-left: 10px;
    height: 40px;
}
.tab {
    display: flex;
    align-items: center;
    padding: 0 10px;
    height: 32px;
    font-size: 13px;
    cursor: pointer;
    border-radius: 6px 6px 0 0;
    margin-right: 4px;
    color: var(--text-color);
    transition: all 0.2s;
}
.tab.active {
    background: #fff;
    color: #409eff;
    font-weight: 500;
    box-shadow: 0 -1px 2px rgba(0,0,0,0.05);
}
.tab .el-icon { margin-right: 5px; }
.tab .close-icon { margin-left: 5px; margin-right: 0; font-size: 10px; }
.tab.add-tab { width: 28px; justify-content: center; padding: 0; }

.toolbar {
    padding: 8px 16px;
    border-bottom: 1px solid var(--border-color);
    background: #fff;
    display: flex;
    justify-content: space-between;
    align-items: center;
    height: 60px;
    box-shadow: var(--shadow-sm);
    z-index: 10;
}
.left-tools {
    display: flex;
    align-items: center;
    gap: 8px;
}
.context-label {
    font-size: 13px;
    color: #606266;
    font-weight: 500;
}
.context-sep {
    font-weight: bold;
    color: #909399;
}
.right-tools {
    display: flex;
    align-items: center;
    gap: 15px;
}
.schema-selector {
    font-size: 12px;
    color: #606266;
    background: #f4f4f5;
    padding: 4px 8px;
    border-radius: 4px;
}
.run-btn {
    background-color: var(--primary-color);
    border-color: var(--primary-color);
    font-weight: 600;
    padding: 8px 16px;
    font-size: 14px;
    box-shadow: var(--shadow-md);
    transition: all 0.2s;
}
.run-btn:hover {
    background-color: var(--primary-hover);
    border-color: var(--primary-hover);
    transform: translateY(-1px);
    box-shadow: 0 4px 6px -1px rgba(37, 99, 235, 0.3);
}
.schema-bar {
    padding: 5px 10px;
    background: #fff;
    border-bottom: 1px solid #ebeef5;
    display: flex;
    align-items: center;
    gap: 10px;
    font-size: 12px;
    color: #606266;
}

/* Bottom Panel */
.bottom-panel {
    height: 100%;
    display: flex;
    flex-direction: column;
}
.bottom-tabs {
    height: 100%;
    display: flex;
    flex-direction: column;
    border: none;
    box-shadow: none;
}
:deep(.el-tabs__content) {
    flex: 1;
    overflow: auto;
    padding: 0;
}
:deep(.el-tabs__header) {
    background: #f5f7fa;
    border-bottom: 1px solid #e4e7ed;
    margin: 0;
}
.history-mock {
    padding: 10px;
}
</style>
