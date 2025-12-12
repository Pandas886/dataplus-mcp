<template>
  <div class="catalog-tree-container">
    <div class="header">
        <span>Data Explorer</span>
        <el-button type="text" @click="refresh">
            <el-icon><Refresh /></el-icon>
        </el-button>
    </div>
    <el-tree
      :props="props"
      :load="loadNode"
      lazy
      @node-click="handleNodeClick"
      highlight-current
    >
      <template #default="{ node }">
        <span class="custom-tree-node">
          <el-icon v-if="node.level === 1"><Files /></el-icon>
          <el-icon v-else-if="node.level === 2"><Folder /></el-icon>
          <el-icon v-else><Document /></el-icon>
          <span style="margin-left: 6px">{{ node.label }}</span>
        </span>
      </template>
    </el-tree>
  </div>
</template>

<script setup lang="ts">
import { Refresh, Files, Folder, Document } from '@element-plus/icons-vue'
import { TrinoService } from '../services/TrinoService'

const emit = defineEmits(['node-click'])

const props = {
  label: 'name',
  children: 'zones',
  isLeaf: 'leaf',
}

// Use any to avoid internal type import issues or strict typing complexity for now
const loadNode = async (node: any, resolve: any) => {
  if (node.level === 0) {
    try {
        const catalogs = await TrinoService.getCatalogs()
        return resolve(catalogs.map((c: string) => ({ name: c, type: 'catalog' })))
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

const refresh = () => {
    // Implementation to reload tree would be complex with el-tree lazy, 
    // simpler to just full reload or unmount/remount in real app
    window.location.reload()
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
    font-weight: bold;
    border-bottom: 1px solid #ebeef5;
    display: flex;
    justify-content: space-between;
    align-items: center;
}
.custom-tree-node {
    display: flex;
    align-items: center;
}
</style>
