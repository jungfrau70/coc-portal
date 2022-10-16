

#############################################################################################
# 1. Install Yarn package manager
#############################################################################################

npm install -g yarn


#############################################################################################
# 2. install dependencies
#############################################################################################

# install dependencies nuxt cli
yarn add nuxt


#############################################################################################
# 3. Create APP
#############################################################################################

mkdir app && cd app

# create package.json
yarn init -y

or 

yarn create nuxt-app .


#############################################################################################
# 4. Configure package.json
#############################################################################################

# add below after main
"scripts": {
  "start": "nuxt"
},


#############################################################################################
# 5. Start APP
#############################################################################################

# run app
yarn start


#############################################################################################
# 6. Install vscode extension
#############################################################################################

Vetur 
HTTP CSS Support
Vue 3 Snippets


<!-- # Add Config jsconfig.js
{
    "include": [
      "./src/**/*"
    ]
} -->


#############################################################################################
# 7. Add folders and files
#############################################################################################

pages
pages/index.vue

layouts
layouts/default.vue

components
components/Table.vue
components/Form.vue

store

and more

#############################################################################################
# 8. Configure nuxt.config.js
#############################################################################################

# install dependencies
yarn add @nuxtjs/vuetify @nuxtjs/axios

# configure Nuxt Env.
cat <<EOF > nuxt.config.js
export default {
    buildModules: [
        "@nuxtjs/vuetify"
    ],
    modules: [
        "@nuxtjs/axios"
    ],
    components: true
}
EOF

#############################################################################################
# 9. coding in pages/index.vue
#############################################################################################

cat <<EOF > pages/index.vue
<template lang="">
    <v-row>
        <v-col>
            <Form />
        </v-col>
        <v-col>
            <Table />
        </v-col>
    </v-row>
</template>
EOF

#############################################################################################
# 10. coding in components/{ Table.vue, Form.vue }
#############################################################################################

# google search with keyword, - nuxtjs/vuetify tutorial
# go to the link - Get started with Vuetify
# select the item as below
  UI Components -> Form inputs & controls -> Forms :: https://vuetifyjs.com/en/components/forms/
  Finally select the one I want