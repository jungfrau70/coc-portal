<template>
  <v-card>
    <v-tabs>
      <v-tab to="/incident/list">리스트</v-tab>
      <!-- <v-tab to="/incident/graph">그래프</v-tab>
      <v-tab to="/incident/dashboard">대시보드</v-tab>
      <v-tab to="/incident/analyzer">분석기</v-tab> -->
    </v-tabs>
    <nuxt-child />
    <v-dialog v-model="dialog">
      <template #[`activator`]="{ on }">
        <v-card-actions class="justify-space-between">
          <v-col sm="2">
            <v-text-field
              v-model="search"
              append-icon="mdi-magnify"
              label="Search"
              class="ml-auto ma-3"
              maxlength="25"
              single-line
              hide-details
            ></v-text-field>
          </v-col>
          <v-btn color="primary" dark class="ml-auto ma-3" v-on="on">
            New Record
            <v-icon small>mdi-plus-circle-outline</v-icon>
          </v-btn>
          <v-btn
            color="primary"
            dark
            class="ml-auto ma-3"
            @click="exportData()"
          >
            Download
            <v-icon small>mdi-arrow-right-circle-outline</v-icon>
          </v-btn>
        </v-card-actions>
      </template>
      <template>
        <v-card v-model="dialogAdd">
          <IncidentDetail
            :editedItem="newItem"
            @submit-item="submitItem"
            @close="close(newItem)"
          />
        </v-card>
      </template>
    </v-dialog>

    <v-data-table
      v-model="selected"
      dense
      :search="search"
      :headers="headers"
      :items="filteredItems"
      :options.sync="options"
      show-select
      item-key="id"
      class="elevation-1"
    >
      <template #[`body.prepend`]>
        <tr>
          <th>
            <v-icon>filters</v-icon>
          </th>

          <th v-for="header in headers" :key="header.text">
            <div>
              <v-select
                v-model="filters[header.value]"
                :items="columnValueList(header.value)"
                flat
                hide-details
                small
                multiple
                clearable
              >
              </v-select>
            </div>
          </th>
        </tr>
      </template>
      <template #[`item.actions`]="{ item }">
        <div class="text-truncate">
          <v-btn icon>
            <v-icon>mdi-dots-vertical</v-icon>
            <v-icon
              small
              class="mr-2"
              color="primary"
              @click="showEditDialog(item)"
            >
              mdi-pencil
            </v-icon>
          </v-btn>
          <v-icon small color="pink" @click="showDeleteDialog(item)">
            mdi-delete
          </v-icon>
        </div>
      </template>
    </v-data-table>

    <!-- Edit dialog -->
    <v-dialog v-model="dialogEdit">
      <v-card>
        <IncidentDetail
          :edited-item="editedItem"
          @submit-item="submitItem"
          @close="close(editedItem)"
        />
      </v-card>
    </v-dialog>

    <!-- delete dialog -->
    <v-dialog v-model="dialogDelete" max-width="500px">
      <v-card>
        <v-card-title>Delete</v-card-title>
        <v-card-text
          >Weet je zeker dat je `{{ itemToDelete.Name }}` wenst te
          verwijderen?</v-card-text
        >
        <v-card-actions>
          <v-btn color="primary" text @click="dialogDelete = false"
            >Close</v-btn
          >
          <v-btn color="primary" text @click="deleteItem()">Delete</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </v-card>
</template>
<script>
import axios from 'axios'
import IncidentDetail from '~/components/IncidentDetail.vue'

export default {
  components: { IncidentDetail },

  data() {
    return {
      search: '',

      headers: [
        // { text: 'Id', value: 'id' },
        { text: 'Year', value: 'year', width: '75' },
        { text: 'Month', value: 'month', width: '100', sortable: true },
        { text: 'Region', value: 'region', width: '100', sortable: true },
        { text: 'AZ', value: 'az', width: '75', sortable: true },
        { text: 'Tenant', value: 'tenant', width: '100', sortable: true },
        // { text: 'Progress', value: 'progress', sortable: true },
        { text: 'Status', value: 'status', width: '100', sortable: true },
        { text: 'Event(Title))', value: 'event', sortable: true },
        {
          text: 'Action(Description)',
          value: 'action',
          sortable: true,
          // width: '240',
        },
        {
          text: 'Occurred_at',
          value: 'occurred_at',
          width: '100',
          sortable: false,
        },
        {
          text: 'Acknowledged_at',
          value: 'acknowledged_at',
          width: '100',
          sortable: false,
        },
        {
          text: 'Propogated_at',
          value: 'propogated_at',
          width: '100',
          sortable: false,
        },
        { text: 'Action', value: 'actions', sortable: false },
      ],

      filters: {
        id: [],
        year: [],
        month: [],
        region: [],
        tenant: [],
        progress: [],
        status: [],
      },

      options: {
        sortBy: ['id'],
        sortDesc: ['true'],
      },

      items: [],
      selected: [],
      currentItems: [],
      newItem: {},
      editedItem: {},

      dialog: false,
      dialogAdd: false,
      dialogEdit: false,
      dialogDelete: false,
      itemToDelete: {},
      // pyodide: null,
      // pyodideLoaded: null,
      output: '',
    }
  },

  computed: {
    filteredItems() {
      return this.items.filter((d) => {
        return Object.keys(this.filters).every((f) => {
          return this.filters[f].length < 1 || this.filters[f].includes(d[f])
        })
      })
    },
  },
  watch: {
    dialogAdd: function () {
      this.newItem = {}
    },
  },
  created() {
    console.log('list created')
    this.loadItems()
  },
  mounted() {
    console.log('list mounted')
  },
  updated() {
    console.log('list updated')
    console.log(this.editedItem.id)
  },

  beforeDestroy() {
    console.log('list beforeDestroy')
  },
  methods: {
    customDatetime(datetime) {
      return this.$moment(datetime).format('YYYY-MM-DD HH:mm')
    },

    submitItem(item) {
      if (item) {
        this.dialogEdit = false
        this.editedItem = {}
      } else {
        this.dialogAdd = false
      }
      this.dialog = false

      // airtable API needs the data to be placed in fields object
      const data = {
        // id: item.id,
        year: item.year,
        month: item.month,
        region: item.region,
        az: item.az,
        tenant: item.tenant,
        shift_start_date: item.shift_start_date,
        shift_type: item.shift_type,
        level_1_engineer1: item.level_1_engineer1,
        level_1_engineer2: item.level_1_engineer2,
        level_2_engineers: item.level_2_engineers,
        how_to_share: item.how_to_share,
        event: item.event,
        action: item.action,
        status: item.status,
        ticket_no: item.ticket_no,
        escalated_to_l3: item.escalated_to_l3,
        comment: item.comment,
        occurred_at: this.customDatetime(item.occurred_at),
        acknowledged_at: this.customDatetime(item.acknowledged_at),
        propogated_at: this.customDatetime(item.propogated_at),
        resolved_at: this.customDatetime(item.resolved_at),
        creator: item.creator,
        reviewer: item.reviewer,
        updater: item.updater,
      }
      console.log(data)

      const id = item.id || null
      let method = 'post'
      let url = `http://localhost:8000/incident`

      // save the record
      // headers: {
      //     Authorization: 'Bearer ' + apiToken,
      //     'Content-Type': 'application/json',
      //   },
      axios[method](url, data, {
        headers: {
          'Access-Control-Allow-Origin': '*',
          'Access-Control-Allow-Methods':
            'GET, POST, PATCH, PUT, DELETE, OPTIONS',
          'Access-Control-Allow-Headers': 'Origin, Content-Type, X-Auth-Token',
          'Content-Type': 'application/json',
        },
      }).then((response) => {
        if (response.data && response.data.id) {
          // add new item to state
          this.editedItem.id = response.data.id
          if (!id) {
            // add the new item to items state
            this.items.push(this.editedItem)
          }
          this.editedItem = {}
        }
        this.dialog = !this.dialog
      })

      if (id) {
        // if the item has an id, we're updating an existing item
        console.log(id)
        method = 'patch'
        url = `http://localhost:8000/incident/${id}`

        // must remove id from the data for airtable patch to work
        delete data.fields.id
      }

    },

    close(item) {
      console.log('list close')
      // this.editedItem = {}
      if (item) {
        this.dialogEdit = false
        this.editedItem = {}
      } else {
        this.dialogAdd = false
      }
      this.dialog = false
    },
    getFiltered(e) {
      this.currentItems = e
    },
    toggleAll() {
      if (this.selected.length) this.selected = []
      else this.selected = this.currentItems.slice()
    },

    changeSort(column) {
      if (this.options.sortBy === column) {
        this.options.descending = !this.options.descending
      } else {
        this.options.sortBy = column
        this.options.descending = false
      }
    },

    columnValueList(val) {
      return this.items.map((d) => d[val])
    },

    showEditDialog(item) {
      if (!item.id) {
        item = {}
      }
      // console.log(item)
      this.editedItem = item || {}
      this.dialogEdit = !this.dialogEdit
    },

    async loadItems() {
      this.items = []
      await axios
        .get('http://localhost:8000/incident/all', {
          headers: {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods':
              'GET, POST, PATCH, PUT, DELETE, OPTIONS',
            'Access-Control-Allow-Headers':
              'Origin, Content-Type, X-Auth-Token',
          },
        })
        .then((response) => {
          this.items = response.data.map((item) => {
            return {
              id: item.id,
              year: item.year,
              month: item.month,
              region: item.region,
              az: item.az,
              tenant: item.tenant,
              shift_start_date: item.shift_start_date,
              shift_type: item.shift_type,
              level_1_engineer1: item.level_1_engineer1,
              level_1_engineer2: item.level_1_engineer2,
              level_2_engineers: item.level_2_engineers,
              how_to_share: item.how_to_share,
              event: item.event,
              action: item.action,
              status: item.status,
              ticket_no: item.ticket_no,
              escalated_to_l3: item.escalated_to_l3,
              comment: item.comment,
              occurred_at: this.customDatetime(item.occurred_at),
              acknowledged_at: this.customDatetime(item.acknowledged_at),
              propogated_at: this.customDatetime(item.propogated_at),
              resolved_at: this.customDatetime(item.resolved_at),
              creator: item.creator,
              reviewer: item.reviewer,
              updater: item.updater,
            }
          })
        })
        .catch((error) => {
          console.log(error)
        })
    },
    // this.item.occurred_at = this.customDatetime(this.item.occurred_at)
    //   this.item.acknowledged_at = this.customDatetime(this.item.occurred_at)
    //   this.item.propogated_at = this.customDatetime(this.item.propogated_at)

    // addItem() {
    //   console.log(this.editedItem)
    //   fetch('http://localhost:8000/incident', {
    //     method: 'POST',
    //     body: JSON.stringify(this.editedItem),
    //     headers: {
    //       'Content-Type': 'application/json',
    //     },
    //   })
    //   // const json = await res.json();
    //   // this.records.push(json);
    //   // this.newRecordText = ''
    // },

    // submitItem(item) {
    //   console.log("submit in list")
    //   // console.log(value)
    // },

    deleteItem() {
      // console.log('deleteItem', this.itemToDelete)
      const index = this.items.indexOf(this.itemToDelete)

      /*
          axios.delete(`https://api.airtable.com/v0/${airTableApp}/${airTableName}/${id}`,
              { headers: {
                  Authorization: "Bearer " + apiToken,
                  "Content-Type": "application/json"
              }
          }).then((response) => {
              this.items.splice(index, 1)
          })
          */

      this.items.splice(index, 1)
      this.dialogDelete = false
    },

    showDeleteDialog(item) {
      this.itemToDelete = item
      this.dialogDelete = !this.dialogDelete
    },

    pivot(arr) {
      const mp = new Map()

      function setValue(a, path, val) {
        if (Object(val) !== val) {
          // primitive value
          const pathStr = path.join('.')
          const i = (mp.has(pathStr) ? mp : mp.set(pathStr, mp.size)).get(
            pathStr
          )
          a[i] = val
        } else {
          for (const key in val) {
            setValue(a, key === '0' ? path : path.concat(key), val[key])
          }
        }
        return a
      }

      const result = arr.map((obj) => setValue([], [], obj))
      return [[...mp.keys()], ...result]
    },

    toCsv(arr) {
      return arr
        .map((row) =>
          row.map((val) => (isNaN(val) ? JSON.stringify(val) : +val)).join(',')
        )
        .join('\n')
    },

    exportData() {
      // Conversion to 2D array and then to CSV:
      // const data = this.toCsv(this.pivot(this.filteredItems))
      let data = []
      if (this.selected.length === 0) {
        data = this.toCsv(this.pivot(this.filteredItems))
      } else {
        // console.log(this.selected)
        data = this.toCsv(this.pivot(this.selected))
      }

      const pom = document.createElement('a')

      const blob = new Blob(['\uFEFF' + data], {
        type: 'text/csv; charset=utf-8',
      })
      const url = URL.createObjectURL(blob)
      pom.href = url
      pom.setAttribute('download', 'export.csv')
      pom.click()
    },

    genReport() {
      // fetch('/plugins/pyodide.html').then((response) => {
      //   console.log(response)
      // })
    },
  },
}
</script>
