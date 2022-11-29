<template>
  <v-app>
    <NavBar title="Products application">
      <template v-slot:drawbtn>
        <v-app-bar-nav-icon @click.stop="drawer = !drawer"></v-app-bar-nav-icon>
      </template>
    </NavBar>
    <v-content style="height: 100vh">
      <v-card>
        <v-layout>
          <v-navigation-drawer v-model="drawer" temporary>
            <v-list-item
              prepend-avatar="https://www.gravatar.com/avatar/302c652af1a74abdadf3dcaebd6513ee?s=120"
              title="About"
              nav
            >
            </v-list-item>

            <v-divider></v-divider>

            <v-list density="compact" nav>
              <v-list-item
                to="/"
                prepend-icon="mdi-home-city"
                title="Home page"
                value="home"
                link
              ></v-list-item>
              <v-list-item
                prepend-icon="mdi-account"
                title="My Account"
                value="account"
              ></v-list-item>
              <v-list-item
                to="/products"
                prepend-icon="mdi-account-group-outline"
                title="Products"
                value="products"
                link
              >
              </v-list-item>
            </v-list>
          </v-navigation-drawer>
          <v-main style="height: 100vh">
            <router-view />
          </v-main>
        </v-layout>
      </v-card>
    </v-content>
    <Footer></Footer>
  </v-app>
</template>
<script>
import Navbar from "./components/navbar.vue";
import Footer from "./components/footer.vue";

export default {
  data: () => ({
    drawer: null,
  }),
  components: {
    NavBar: Navbar,
    Footer: Footer,
  },
};
</script>
