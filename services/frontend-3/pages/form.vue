<template>
  <v-form v-model="valid">
    <v-container>
      <v-row>
        <v-col
          v-for="(options, index) in colOptions"
          :key="index"
          cols="12"
          md="2"
        >
          <v-select
            v-model="item[index]"
            :items="options"
            :label="index"
            required
          >
          </v-select>
        </v-col>
      </v-row>
      <v-row>
        <h1>{{ item['year'] }}년 {{ item['month'] }}월</h1>
      </v-row>
    </v-container>
  </v-form>
</template>

<script>
export default {
  data() {
    return {
      valid: true,
      item: {
        year: 2022,
        month: 1,
        region: 'KR',
        az: 1,
        tenant: 'PRD',
        status: 'created',
      },

      colOptions: {
        year: [2022, 2023, 2024, 2025],
        month: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
        region: ['KR', 'EU'],
        az: [1, 2],
        tenant: ['PRD', 'PRE_PRD', 'STG', 'DEV'],
        status: ['created', 'in-process', 'completed', 'cancelled', 'delayed'],
      },
    }
  },
}
</script>
