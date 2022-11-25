<template>
  <v-card>
    <v-card-title>
      <v-text-field
        v-model="search"
        append-icon="mdi-magnify"
        label="Search"
        single-line
        hide-details
      ></v-text-field>
    </v-card-title>

    <v-data-table
      :search="search"
      :headers="headers"
      :filtered_items="filtered_items"
      :items="items"
      :sort-by="['year', 'month']"
      :sort-desc="[false, false]"
      class="elevation-1"
    >
      <template #top>
        <v-toolbar flat>
          <v-toolbar-title>Problem</v-toolbar-title>
          <v-divider class="mx-4" inset vertical></v-divider>
          <v-spacer></v-spacer>
          <v-dialog v-model="dialog" max-width="500px">
            <template #activator="{ on, attrs }">
              <v-btn color="primary" dark class="mb-2" v-bind="attrs" v-on="on">
                New Item
              </v-btn>
            </template>
            <v-card>
              <v-card-title>
                <span class="text-h5">{{ formTitle }}</span>
              </v-card-title>
              <v-card-text>
                <v-container>
                  <v-row>
                    <v-col cols="80" sm="6" md="4">
                      <v-text-field
                        v-model="editedItem.title"
                        label="Title"
                      ></v-text-field>
                    </v-col>
                    <v-col cols="80" sm="6" md="4">
                      <v-text-field
                        v-model="editedItem.description"
                        label="Description"
                      ></v-text-field>
                    </v-col>
                    <v-col cols="80" sm="6" md="4">
                      <v-text-field
                        v-model="editedItem.impact"
                        label="Impact"
                      ></v-text-field>
                    </v-col>
                    <v-col cols="80" sm="6" md="4">
                      <v-text-field
                        v-model="editedItem.review_desc"
                        label="Review"
                      ></v-text-field>
                    </v-col>
                    <v-col cols="80" sm="6" md="4">
                      <v-text-field
                        v-model="editedItem.rca_desc"
                        label="RCA"
                      ></v-text-field>
                    </v-col>
                  </v-row>
                </v-container>
              </v-card-text>

              <v-card-actions>
                <v-spacer></v-spacer>
                <v-btn color="blue darken-1" text @click="close">
                  Cancel
                </v-btn>
                <v-btn color="blue darken-1" text @click="save"> Save </v-btn>
              </v-card-actions>
            </v-card>
          </v-dialog>
          <v-dialog v-model="dialogDelete" max-width="500px">
            <v-card>
              <v-card-title class="text-h5"
                >Are you sure you want to delete this item?</v-card-title
              >
              <v-card-actions>
                <v-spacer></v-spacer>
                <v-btn color="blue darken-1" text @click="closeDelete"
                  >Cancel</v-btn
                >
                <v-btn color="blue darken-1" text @click="deleteItemConfirm"
                  >OK</v-btn
                >
                <v-spacer></v-spacer>
              </v-card-actions>
            </v-card>
          </v-dialog>
        </v-toolbar>
      </template>
      <template #item.actions="{ item }">
        <v-icon small class="mr-2" @click="editItem(item)"> mdi-pencil </v-icon>
        <v-icon small @click="deleteItem(item)"> mdi-delete </v-icon>
      </template>
      <template #no-data>
        <v-btn color="primary" @click="fetchData"> Reset </v-btn>
      </template>
    </v-data-table>
  </v-card>
</template>

<script>
import axios from 'axios'

export default {
  data: () => ({
    search: '',
    dialog: false,
    dialogDelete: false,

    headers: [],
    items: [],
    filtered_items: [],
    sortIndex: null,
    sortDirection: null,

    totalRows: 1,
    currentPage: 1,
    perPage: 10,
    pageOptions: [10, 10, 30, { value: 100, text: 'Show a lot' }],

    editedIndex: -1,
    editedItem: {
      title: '',
      description: '',
      impact: '',
      review_desc: '',
      rca_desc: '',
    },
    defaultItem: {
      title: '',
      description: '',
      impact: '',
      review_desc: '',
      rca_desc: '',
    },
  }),

  headers() {
    let s = new Set()

    this.items.forEach((item) => {
      for (f in item) {
        s.add(f)
      }
    })

    return Array.from(s).map((a) => {
      return {
        text: a.toUpperCase(),
        value: a,
      }
    })
  },

  computed: {
    formTitle() {
      return this.editedIndex === -1 ? 'New Item' : 'Edit Item'
    },
  },

  watch: {
    dialog(val) {
      val || this.close()
    },
    dialogDelete(val) {
      val || this.closeDelete()
    },
  },

  created() {
    this.fetchData()
  },

  mounted() {
    this.filtered_items = [...this.items]
    // Set the initial number of items
    this.totalRows = this.filtered_items.length
    console.log(this.totalRows)
  },

  methods: {
    async fetchData() {
      await axios
        .get('http://localhost:8000/problem/all', {
          headers: {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods':
              'GET, POST, PATCH, PUT, DELETE, OPTIONS',
            'Access-Control-Allow-Headers':
              'Origin, Content-Type, X-Auth-Token',
          },
        })
        .then((res) => {
          this.items = res.data
        })
        .catch((err) => {
          console.log(err)
        })

      this.headers = Object.keys(this.items[0])
      console.log(this.headers)
      // this.rows = this.rawRows.data
    },

    editItem(item) {
      this.editedIndex = this.desserts.indexOf(item)
      this.editedItem = Object.assign({}, item)
      this.dialog = true
    },

    deleteItem(item) {
      this.editedIndex = this.desserts.indexOf(item)
      this.editedItem = Object.assign({}, item)
      this.dialogDelete = true
    },

    deleteItemConfirm() {
      this.desserts.splice(this.editedIndex, 1)
      this.closeDelete()
    },

    close() {
      this.dialog = false
      this.$nextTick(() => {
        this.editedItem = Object.assign({}, this.defaultItem)
        this.editedIndex = -1
      })
    },

    closeDelete() {
      this.dialogDelete = false
      this.$nextTick(() => {
        this.editedItem = Object.assign({}, this.defaultItem)
        this.editedIndex = -1
      })
    },

    save() {
      if (this.editedIndex > -1) {
        Object.assign(this.desserts[this.editedIndex], this.editedItem)
      } else {
        this.desserts.push(this.editedItem)
      }
      this.close()
    },
  },
}
</script>
