<template>
  <v-app>
    <NavBar title="Products application">
      <template v-slot:drawbtn>
       <v-app-bar-nav-icon @click.stop="drawer = !drawer"></v-app-bar-nav-icon>
      </template>
    </NavBar>
    <v-content style="height: 100vh">
      <v-card style="height: 100vh">
        <v-layout>
          <v-navigation-drawer v-model="drawer" temporary>
            <v-list-item
              prepend-avatar="https://randomuser.me/api/portraits/men/84.jpg"
              title="John Leider"
              nav
            >
            </v-list-item>

            <v-divider></v-divider>

            <v-list density="compact" nav>
              <v-list-item
                prepend-icon="mdi-home-city"
                title="Home"
                value="home"
              ></v-list-item>
              <v-list-item
                prepend-icon="mdi-account"
                title="My Account"
                value="account"
              ></v-list-item>
              <v-list-item
                prepend-icon="mdi-account-group-outline"
                title="Users"
                value="users"
              ></v-list-item>
            </v-list>
          </v-navigation-drawer>
          <v-main style="height: 250px"></v-main>
        </v-layout>
        <router-view />
      </v-card>
    </v-content>
    <Footer></Footer>
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
