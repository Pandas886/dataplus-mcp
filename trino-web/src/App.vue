<template>
  <div class="main-layout">
    <splitpanes class="default-theme">
      <pane size="20" min-size="10">
        <CatalogTree @node-click="handleNodeClick" />
      </pane>
      <pane>
        <splitpanes horizontal>
          <pane size="60">
            <div class="editor-container">
               <div class="toolbar">
                 <el-button type="primary" size="small" @click="runQuery" :loading="loading">
                   <el-icon><VideoPlay /></el-icon> Run
                 </el-button>
               </div>
               <SqlEditor v-model="currentSql" />
            </div>
          </pane>
          <pane size="40">
            <ResultsTable :data="queryResult" :loading="loading" :error="error" />
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

const handleNodeClick = (node: any) => {
  if (node.type === 'table') {
    // Generate a select query for the table
    currentSql.value = `SELECT * FROM "${node.catalog}"."${node.schema}"."${node.name}" LIMIT 100`
  }
}

const runQuery = async () => {
    loading.value = true
    error.value = ''
    queryResult.value = null
    try {
        const res = await TrinoService.execute(currentSql.value)
        
        // Transform for table component
        // The service returns { columns: [...], rows: [...] } matching what we need mostly
        // but let's ensure it matches exactly the prop structure
        queryResult.value = {
            id: res.id,
            columns: res.columns, 
            rows: res.rows
        }
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
}
.editor-container {
    height: 100%;
    display: flex;
    flex-direction: column;
}
.toolbar {
    padding: 8px;
    border-bottom: 1px solid #dcdfe6;
    background: #f5f7fa;
    display: flex;
    justify-content: flex-end;
}
</style>
