<template>
  <div class="d-flex align-center flex-column">
    <br />
    <v-card width="400">
      <v-img
        src="https://cdn.vuetifyjs.com/images/cards/sunshine.jpg"
        height="150px"
        cover
      ></v-img>
      <v-card-title> Pervolare test </v-card-title>
      <v-card-subtitle> listar productos y atributos </v-card-subtitle>
      <v-card-actions>
        <v-btn color="green-lighten-2" variant="text"
        to="/signin" link>sign in</v-btn>

        <v-spacer></v-spacer>
        <v-btn color="orange-lighten-2" variant="text"
        to="/signup" link>sign up</v-btn>
      </v-card-actions>
    </v-card>
  </div>
</template>

<script>
</script>
