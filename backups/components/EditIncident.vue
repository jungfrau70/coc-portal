<template>
  <v-card>
    <v-card-title>
      <span v-if="editedItem.id">Edit {{ editedItem.id }}</span>
      <span v-else>Create</span>
    </v-card-title>
    <v-card-text>
      <v-row>
        <v-col cols="12" sm="4">
          <v-text-field v-model="editedItem.title" label="Title"></v-text-field>
        </v-col>
        <v-col cols="12" sm="8">
          <v-text-field
            v-model="editedItem.description"
            label="Description"
          ></v-text-field>
        </v-col>
        <v-col cols="12" sm="12">
          <v-text-field
            v-model="editedItem.status"
            label="Status"
          ></v-text-field>
        </v-col>
      </v-row>
    </v-card-text>
    <v-card-actions>
      <v-spacer></v-spacer>
      <v-btn color="blue darken-1" text @click="showEditDialog()">Cancel</v-btn>
      <v-btn color="blue darken-1" text @click="saveItem(editedItem)"
        >Save</v-btn
      >
    </v-card-actions>
  </v-card>

  <!-- <v-row justify="center"> -->
  <!-- <v-list-item>
      <v-list-item-content>
        <v-list-item-title>{{ editedItem.title }}</v-list-item-title>
        <v-list-item-subtitle
          >Set the content filtering level to restrict apps that can be
          downloaded</v-list-item-subtitle
        >

        <v-div> {{ item.description }}</v-div>
        <v-card-text>
          <v-row>
            <v-col cols="12" sm="4">
              <v-text-field
                v-model="editedItem.title"
                label="Name"
              ></v-text-field>
            </v-col>
            <v-col cols="12" sm="8">
              <v-text-field
                v-model="editedItem.Description"
                label="Details"
              ></v-text-field>
            </v-col>
            <v-col cols="12" sm="12">
              <v-text-field v-model="editedItem.status" label="URL"></v-text-field>
            </v-col>
          </v-row>
        </v-card-text>
      </v-list-item-content>
    </v-list-item> -->
  <!-- <v-card>
      <v-list three-line subheader class="product">
        <v-subheader>User Controls</v-subheader>
        <v-list-item>
          <v-list-item-content>
            <v-list-item-title>{{ product.title }}</v-list-item-title>
            <v-list-item-subtitle
              >Set the content filtering level to restrict apps that can be
              downloaded</v-list-item-subtitle
            >

            <v-div> {{ product.price }}</v-div>
          </v-list-item-content>
        </v-list-item>
      </v-list>
    </v-card> -->
  <!-- </v-row> -->
</template>

<script>
export default {
  name: 'NewAndEdit',
  props: {
    editedItem: {
      type: Object,
      default: null,
    },
  },
  methods: {
    showEditDialog(item) {
      this.editedItem = item || {}
      this.dialog = !this.dialog
    },
  },
}
</script>
