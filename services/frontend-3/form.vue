<template>
  <v-form ref="form" v-model="valid" lazy-validation>
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
        <v-col>
          <v-datetime-picker v-model="item['occurred_at']" label="Occurred_at">
          </v-datetime-picker>
        </v-col>
        <v-col>
          <v-datetime-picker
            v-model="item['acknowledged_at']"
            label="Acknowledged_at"
          >
          </v-datetime-picker>
        </v-col>
        <v-col>
          <v-datetime-picker
            v-model="item['propogated_at']"
            label="Propogated_at"
          >
          </v-datetime-picker>
        </v-col>
      </v-row>

      <!-- <v-row>
        <h1>
          {{ item['year'] }}년 {{ item['month'] }}월, {{ item['occurred_at'] }},
          {{ item['acknowledged_at'] }}, {{ item['propograted_at'] }},
        </h1>
      </v-row> -->

      <v-row>
        <v-text-field
          v-model="item['title']"
          label="Title"
          required
        ></v-text-field>
      </v-row>
      <v-row>
        <v-textarea
          v-model="item['info']"
          filled
          label="Info"
          auto-grow
          value="The Woodman set to work at once, and so sharp was his axe that the tree was soon chopped nearly through."
        ></v-textarea>
      </v-row>
      <v-row>
        <v-textarea
          v-model="item['action']"
          filled
          label="Action"
          auto-grow
          value="The Woodman set to work at once, and so sharp was his axe that the tree was soon chopped nearly through."
        ></v-textarea>
      </v-row>
              <v-card-text style="height: 100px; position: relative">
            <v-fab-transition>
              <v-btn
                v-show="!hidden"
                color="pink"
                dark
                absolute
                top
                right
                fab
              >
                <v-icon>mdi-plus</v-icon>
              </v-btn>
            </v-fab-transition>
          </v-card-text>
    </v-container>
  </v-form>
</template>

<script>
export default {
  components: {},
  data: (vm) => ({
    valid: true,
    item: {
      year: 2022,
      month: 1,
      region: 'KR',
      az: 1,
      tenant: 'PRD',
      status: 'created',
      occurred_at: null,
      acknowledged_at: null,
      propogated_at: null,
      updated_at: null,
      title: null,
      info: null,
      action: null,
      escalated_to_2l: null,
      escalated_to_3l: null,
    },

    colOptions: {
      year: [2022, 2023, 2024, 2025],
      month: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
      region: ['KR', 'EU'],
      az: [1, 2],
      tenant: ['PRD', 'PRE_PRD', 'STG', 'DEV'],
      status: ['created', 'in-process', 'completed', 'cancelled', 'delayed'],
    },
    // date: new Date(Date.now() - new Date().getTimezoneOffset() * 60000)
    //   .toISOString()
    //   .substr(0, 10),
    // dateFormatted: vm.formatDate(
    //   new Date(Date.now() - new Date().getTimezoneOffset() * 60000)
    //     .toISOString()
    //     .substr(0, 10)
    // ),
    // menu1: false,
    // menu2: false,
  }),
  // computed: {
  //   computedDateFormatted() {
  //     return this.formatDate(this.date)
  //   },
  // },
  // watch: {
  //   date(val) {
  //     this.dateFormatted = this.formatDate(this.date)
  //   },
  // },
  // methods: {
  //   formatDate(date) {
  //     if (!date) return null

  //     const [year, month, day] = date.split('-')
  //     return `${month}/${day}/${year}`
  //   },
  //   parseDate(date) {
  //     if (!date) return null

  //     const [month, day, year] = date.split('/')
  //     return `${year}-${month.padStart(2, '0')}-${day.padStart(2, '0')}`
  //   },
  // },
}
</script>
