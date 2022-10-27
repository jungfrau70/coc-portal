<template>
   <v-app id="inspire">
      <v-main>
         <v-container fluid fill-height>
            <v-layout align-center justify-center>
               <v-flex > <!-- xs12 sm8 md4 -->
                  <v-card class="elevation-12">
                     <v-toolbar dark color="primary">
                        <v-toolbar-title>Login</v-toolbar-title>
                     </v-toolbar>
                     <v-card-text>
                        <v-form>
                           <v-text-field
                              name="username"
                              label="Username"
                              type="email"
                              v-model="username"
                              placeholder="Email" 
                              required
                           ></v-text-field>
                           <v-text-field
                              name="password"
                              label="Password"
                              type="password"
                              v-model="password"
                              placeholder="Password"
                              required
                           ></v-text-field>
                        </v-form>
                     </v-card-text>
                     <v-card-actions>
                        <v-spacer></v-spacer>
                        <v-btn color="primary" @click="loginHandler">Login</v-btn>
                     </v-card-actions>
                  </v-card>
               </v-flex>
            </v-layout>
         </v-container>
      </v-main>
   </v-app>
</template>

<script>
   export default {
      name: "login",
      data() {
         return {
            password: '',
            nameRules: [
            v => !!v || 'Name is required',
            v => (v && v.length <= 10) || 'Name must be less than 10 characters',
            ],
            username: '',
            emailRules: [
            v => !!v || 'E-mail is required',
            v => /.+@.+\..+/.test(v) || 'E-mail must be valid',
            ],            
         }
      },

      methods: {
         async loginHandler() {
            const data = { 'username': this.username, 'password': this.password }
            console.log(data);
            try{        
               const response = await this.$auth.loginWith('local', { data: data})
               console.log(response)       
               this.$auth.$storage.setUniversal('bearer', response.data.access_token)
               await this.$auth.setUserToken(response.data.access_token, response.data.refresh_token)

            } catch(e) {
               console.log(e.message)
            }
            await this.$router.push('/');         
         }
      }      
      
      // methods: {
      //    async loginHandler() {
      //       try{        
      //          const response = await fetch('http://localhost:8000/account/login', {
      //             method: 'POST',
      //             headers: {'Content-Type': 'application/json'},
      //             credentials: 'include',
      //             body: JSON.stringify({
      //                username: this.username,
      //                password: this.password
      //             })})
      //          console.log(response)       
      //          // this.$auth.$storage.setUniversal('bearer', response.data.access_token)
      //          // await this.$auth.setUserToken(response.data.access_token, response.data.refresh_token)

      //       } catch(e) {
      //          console.log(e.message)
      //       }
      //       await this.$router.push('/');
      //    }
      // }
   }
</script>

<style></style>
