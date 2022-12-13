<template>
  <v-card>
    <v-card-title>
      <span v-if="editedItem.id">Edit {{ editedItem.id }}</span>
      <span v-else>Create</span>
    </v-card-title>
    <v-card-text>
      <v-row>
        <v-col cols="12" sm="2">
          <v-text-field v-model="item.year" label="Year"></v-text-field>
        </v-col>
        <v-col cols="12" sm="2">
          <v-text-field v-model="item.month" label="Month"></v-text-field>
        </v-col>
        <v-col cols="12" sm="2">
          <v-text-field v-model="item.region" label="Region"></v-text-field>
        </v-col>
        <v-col cols="12" sm="2">
          <v-text-field v-model="item.tenant" label="Tenant"></v-text-field>
        </v-col>
        <v-col cols="12" sm="2">
          <v-text-field v-model="item.progress" label="Porgress"></v-text-field>
        </v-col>
        <v-col cols="12" sm="2">
          <v-text-field v-model="item.status" label="Status"></v-text-field>
        </v-col>
      </v-row>
      <v-spacer></v-spacer>
      <v-row>
        <v-col cols="12" sm="4">
          <v-text-field v-model="item.title" label="Title"></v-text-field>
        </v-col>
      </v-row>
      <v-row>
        <v-col cols="12" sm="8">
          <v-text-field
            v-model="item.description"
            label="Description"
          ></v-text-field>
          <!-- <div v-highlight v-html="$md.render(''+item.description)"></div> -->
          <div v-html="$md.render(''+item.description)"></div>
        </v-col>
      </v-row>
    </v-card-text>
  </v-card>
</template>

<script>
export default {
  name: 'EditIncident',
  props: {
    editedItem: {
      type: Object,
      default: null,
    },
  },
  data() {
    return {
      item: {},
      convertedText: '',
    }
  },
  updated() {
    this.loadItem()
  },
  methods: {
    loadItem() {
      this.item = this.editedItem || {}
      this.$emit('showEditDialog', this.item)
    },
  },
}
</script>
