<template>
  <v-app>
    <v-main>
      <NavBar title="Products application"></NavBar>
      <v-content style="height: 100vh">
        <v-container
          fluid
          pa-0
          class="d-flex flex-column flex-grow-1 fill-parent-height"
        >
          <router-view />
        </v-container>
      </v-content>
      <Footer></Footer>
    </v-main>
  </v-app>
</template>
<script>
import Navbar from "./components/navbar.vue";
import Footer from "./components/footer.vue";

export default {
  components: {
    NavBar: Navbar,
    Footer: Footer,
  },
};
</script>
