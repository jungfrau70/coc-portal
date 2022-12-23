<template >
  <v-card>
    <v-form ref="form" v-model="valid" lazy-validation>
      <v-container>
        <v-row>
          <v-card-title>
            <span v-if="editedItem.id">Edit {{ editedItem.id }}</span>
            <span v-else>Create</span>
          </v-card-title>
        </v-row>
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
            <v-datetime-picker
              v-model="item['occurred_at']"
              :formatter="DatetimePickerFormat"
              label="Occurred_at"
            >
            </v-datetime-picker>
          </v-col>
          <v-col>
            <v-datetime-picker
              v-model="item['acknowledged_at']"
              :formatter="DatetimePickerFormat"
              label="Acknowledged_at"
            >
            </v-datetime-picker>
          </v-col>
          <v-col>
            <v-datetime-picker
              v-model="item['propogated_at']"
              :formatter="DatetimePickerFormat"
              label="Propogated_at"
            >
            </v-datetime-picker>
          </v-col>
        </v-row>

        <v-row>
          <v-text-field
            v-model="item['event']"
            label="Title(Event)"
            required
          ></v-text-field>
        </v-row>
        <v-row>
          <v-col>
            <v-textarea
              v-model="item['action']"
              filled
              label="Action"
              auto-grow
              value="The Woodman set to work at once, and so sharp was his axe that the tree was soon chopped nearly through."
            ></v-textarea>
          </v-col>
          <v-col>
            <template>
              <div v-html="actionMarkdown"></div>
            </template>
          </v-col>
        </v-row>
        <v-row>
          <v-col>
            <v-textarea
              v-model="item['comment']"
              filled
              label="Comment"
              auto-grow
              value="The Woodman set to work at once, and so sharp was his axe that the tree was soon chopped nearly through."
            ></v-textarea>
          </v-col>
          <!-- <v-col>
            <div v-html="changeMarkdown"></div>
          </v-col> -->
        </v-row>
        <v-spacer></v-spacer>
        <v-row>
          <v-btn class="mr-4" color="green darken-1" @click="submitItem"
            >Submit</v-btn
          >
          <v-btn color="dark darken-1" @click="close(editedItem.id)"
            >Close</v-btn
          >
        </v-row>

        <v-card-text style="height: 100px; position: relative">
          <v-fab-transition>
            <v-btn v-show="!hidden" color="pink" dark absolute top right fab>
              <v-icon>mdi-plus</v-icon>
            </v-btn>
          </v-fab-transition>
        </v-card-text>
      </v-container>
    </v-form>
  </v-card>
</template>

<script>
export default {
  name: 'IncidentDetail',
  props: {
    editedItem: {
      type: Object,
      default: null,
    },
  },
  data: (vm) => ({
    // data() {
    //   return {
    dialog: '',
    hidden: true,
    valid: true,
    convertedText: '',
    currentDatetime: null,
    DatetimePickerFormat: 'yyyy-MM-dd HH:mm',
    item: {
      // id: null,
      year: null,
      month: null,
      region: null,
      az: null,
      tenant: null,
      shift_start_date: null,
      shift_type: null,
      level_1_engineer1: null,
      level_1_engineer2: null,
      level_2_engineers: null,
      how_to_share: null,
      event: null,
      action: '# Action Required?',
      status: null,
      ticket_no: null,
      escalated_to_l3: null,
      comment: '# Please comment here',
      occurred_at: null,
      acknowledged_at: null,
      propogated_at: null,
      resolved_at: null,
      creator: null,
      reviewer: null,
      updater: null,
    },
    colOptions: {
      year: [2022, 2023, 2024, 2025],
      month: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
      region: [
        'KR',
        'EU',
        'NA',
        'SG',
        'IN',
        'RU',
        'CN',
        'KR2',
        'KR Bigdata',
        'KR R&D',
      ],
      az: [1, 2, 3, 4, 5, 6, 7, 8],
      tenant: ['PRD', 'PRE_PRD', 'STG', 'DEV', 'bigdata', 'stg', 'prd'],
      status: [
        'created',
        'in-process',
        'completed',
        'cancelled',
        'delayed',
        '완료',
        'NaN',
      ],
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
    // }),
    // filters: {
    //   moment: function (date) {
    //     return this.moment(date).format('MMMM Do YYYY, h:mm:ss a')
    //   },
    // },
  }),
  computed: {
    selected: {
      get() {
        return this.value
      },
      set(value) {
        this.$emit('input', value)
      },
    },
    computedDateFormatted() {
      return this.formatDate(this.date)
    },
    actionMarkdown() {
      // marked.setOptions({
      //   renderer: new marked.Renderer(),
      //   gfm: true,
      //   headerIds: false,
      //   tables: true,
      //   breaks: true,
      //   pedantic: false,
      //   sanitize: true,
      //   smartLists: true,
      //   smartypants: false
      // });
      // return marked(this.item.action);
      return this.$md.render(this.item.action)
    },
  },
  watch: {
    date(val) {
      this.value = this.formatDate(this.date)
    },
  },
  created() {
    console.log('detail created')
    if (this.editedItem.id) {
      this.loadItem()
    } else {
      this.setDefaultItem()
    }
  },
  mounted() {
    console.log('detail mounted')
  },
  updated() {
    console.log('detail updated')
    if (this.editedItem.id) {
      this.loadItem()
    }
  },
  beforeDestroy() {
    console.log('detail beforeDestoryed')
  },
  methods: {
    customDatetime(datetime) {
      return this.$moment(datetime).format('YYYY-MM-DD HH:mm')
    },
    setDefaultItem() {
      console.log('set default values to item')
      this.item.year = this.item.year || 2022
      this.item.month = this.item.month || 1
      this.item.region = this.item.region || 'KR'
      this.item.az = this.item.az || 1
      this.item.tenant = this.item.tenant || 'PRD'
      this.item.shift_start_date = null
      this.item.shift_type = null
      this.item.level_1_engineer1 = null
      this.item.level_1_engineer2 = null
      this.item.level_2_engineers = null
      this.item.how_to_share = null
      this.item.event = null
      this.item.action = '# Action Required?'
      this.item.status = this.item.status || 'created'
      this.item.ticket_no = null
      this.item.escalated_to_l3 = null
      this.item.comment = '# Please comment here'
      this.item.occurred_at = null
      this.item.acknowledged_at = this.item.acknowledged_at || this.getNow()
      this.item.propogated_at = null
      this.item.resolved_at = null
      this.item.creator = null
      this.item.reviewer = null
      this.item.updater = null
    },
    resetItem() {
      this.item = {}
    },
    // formatDate(date) {
    //   if (!date) {
    //     return null
    //   }
    //   return date
    // },
    // parseDate(date) {
    //   if (!date) {
    //     return null
    //   }
    //   const [year, month, day] = date.split('-')
    //   return `${year}-${month.padStart(2, '0')}-${day.padStart(2, '0')}`
    // },
    getNow() {
      const today = new Date()
      const date =
        today.getFullYear() +
        '-' +
        (today.getMonth() + 1) +
        '-' +
        today.getDate()
      const time = today.getHours() + ':' + today.getMinutes()
      // const time = today.getHours() + ':' + today.getMinutes() + ':' + today.getSeconds()
      const timestamp = date + ' ' + time
      return timestamp
    },
    loadItem() {
      this.item = this.editedItem || {}
      this.$emit('showEditDialog', this.item)
      // console.log(this)
    },
    submitItem() {
      this.item = this.editedItem || {}
      this.$emit('submit-item')
      this.resetItem()
    },
    close(id) {
      console.log('detail close')
      this.item = {}
      this.setDefaultItem()

      this.$emit('close', id)
    },
  },
}
</script>
