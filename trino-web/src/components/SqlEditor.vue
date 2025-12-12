<template>
  <div class="sql-editor-wrapper">
    <codemirror
      v-model="code"
      placeholder="Wait for it..."
      :style="{ height: '100%', fontSize: '14px' }"
      :autofocus="true"
      :indent-with-tab="true"
      :tab-size="4"
      :extensions="extensions"
      @ready="handleReady"
      @change="handleChange"
      @focus="handleFocus"
      @blur="handleBlur"
    />
  </div>
</template>

<script setup lang="ts">
import { ref, shallowRef, watch } from 'vue'
import { Codemirror } from 'vue-codemirror'
import { sql } from '@codemirror/lang-sql'
const extensions = [sql()]

const props = defineProps({
  modelValue: {
    type: String,
    default: ''
  }
})

const emit = defineEmits(['update:modelValue'])

const code = ref(props.modelValue)

// View binding
const view = shallowRef()
const handleReady = (payload: any) => {
  view.value = payload.view
}

// Sync prop to internal
watch(() => props.modelValue, (newVal) => {
    if (newVal !== code.value) {
        code.value = newVal
    }
})

const handleChange = (val: string) => {
    emit('update:modelValue', val)
}

const handleFocus = () => {}
const handleBlur = () => {}

</script>

<style scoped>
.sql-editor-wrapper {
    flex: 1;
    overflow: hidden;
    height: 100%;
}
</style>
