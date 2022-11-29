<template>
  <div class="d-flex align-center flex-column">
    <br />
    <v-card width="450">
      <v-img
        src="https://cdn.vuetifyjs.com/images/cards/sunshine.jpg"
        height="150px"
        cover
      ></v-img>
      <v-card-title> Sign in</v-card-title>
      <v-divider></v-divider>
      <v-card-content>
        <v-form v-model="valid">
          <v-container>
            <v-row dense>
              <v-col cols="12" md="6">
                <v-text-field
                  v-model="nombre_completo"
                  :rules="nameRules"
                  :counter="10"
                  label="Fullname"
                  required
                ></v-text-field>
              </v-col>
              <v-col cols="12" md="6">
                <v-text-field
                  v-model="cedula"
                  :rules="nameRules"
                  :counter="10"
                  label="Card Id"
                  required
                ></v-text-field>
              </v-col>
              <v-col cols="12" md="6">
                <v-text-field
                  v-model="departamento"
                  :rules="nameRules"
                  :counter="10"
                  label="Country"
                  required
                ></v-text-field>
              </v-col>
              <v-col cols="12" md="6">
                <v-text-field
                  v-model="municipio"
                  :rules="nameRules"
                  :counter="10"
                  label="State"
                  required
                ></v-text-field>
              </v-col>
              <v-col cols="12" md="6">
                <v-text-field
                  v-model="direccion"
                  :rules="nameRules"
                  :counter="10"
                  label="Address"
                  required
                ></v-text-field>
              </v-col>
              <v-col cols="12" md="6">
                <v-text-field
                  v-model="email"
                  :rules="emailRules"
                  label="E-mail"
                  required
                ></v-text-field>
              </v-col>
              <v-col cols="12" md="6">
                <v-text-field
                  v-model="password"
                  :rules="passwordRules"
                  type="password"
                  label="Password"
                  required
                ></v-text-field>
              </v-col>
            </v-row>
          </v-container>
        </v-form>
      </v-card-content>
      <v-divider></v-divider>
      <v-card-actions>
        <v-btn color="red" @click="cleandata">Clean</v-btn>
        <v-spacer></v-spacer>
        <v-btn color="green">Start now</v-btn>
      </v-card-actions>
    </v-card>
  </div>
</template>
<script>
export default {
  data: () => ({
    valid: false,
    nombre_completo: null,
    cedula: null,
    departamento: null,
    municipio: null,
    direccion: null,
    email: null,
    password: null,
    nameRules: [
      (v) => !!v || "Name is required",
      (v) => v.length <= 10 || "Name must be less than 10 characters",
    ],
    emailRules: [
      (v) => !!v || "E-mail is required",
      (v) => /.+@.+/.test(v) || "E-mail must be valid",
        ],
    passwordRules: [
      (v) => !!v || "PAssword is required",
      (v) => /.+@.+/.test(v) || "password must be valid",
    ],
    }),
    methods: {
        cleandata() {
            this.nombre_completo = null
            this.cedula = null
            this.departamento = null
            this.municipio = null
            this.direccion = null
            this.email = null
            this.password = null
            this.valid = false
         }
    }
};
</script>
