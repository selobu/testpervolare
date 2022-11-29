<template>
  <v-card color="grey-lighten-4" flat height="200px" rounded="0">
    <v-toolbar density="compact">
      <v-app-bar-nav-icon @click.stop="drawer = !drawer"></v-app-bar-nav-icon>

      <v-toolbar-title>{{ title }}</v-toolbar-title>

      <v-spacer></v-spacer>

      <v-btn icon>
        <v-icon>mdi-magnify</v-icon>
      </v-btn>

      <v-btn icon>
        <v-icon>mdi-heart</v-icon>
      </v-btn>

      <v-btn icon >
        <v-icon>mdi-dots-vertical</v-icon>
      </v-btn>
    </v-toolbar>
    <v-card>
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
    </v-card>
  </v-card>
</template>
<script>
export default {
  props: { title: { type: String, required: true } },
  data: () => ({
    drawer: null,
    items: [
      { title: "Home", icon: "mdi-home-city" },
      { title: "My Account", icon: "mdi-account" },
      { title: "Users", icon: "mdi-account-group-outline" },
    ],
  }),
};
</script>