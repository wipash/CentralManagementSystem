<template>
  <v-app>
    <v-navigation-drawer clipped app fixed v-model="drawer">
      <v-list>
        <v-list-tile :key="i" :to="item.to" exact router v-for="(item, i) in items">
          <v-list-tile-action>
            <v-icon>{{ item.icon }}</v-icon>
          </v-list-tile-action>
          <v-list-tile-content>
            <v-list-tile-title v-text="item.title"/>
          </v-list-tile-content>
        </v-list-tile>
      </v-list>
    </v-navigation-drawer>
    <v-toolbar clipped-left app dark fixed color="primary">
      <v-toolbar-side-icon @click="drawer = !drawer"/>
      <img src="/images/logo_white.png" height="50px"  />
      <v-toolbar-title v-text="title" />
      <v-spacer></v-spacer>
      <v-menu open-on-hover top offset-y>
        <template v-slot:activator="{ on }">
          <v-btn fab flat icon>
            <v-icon>user</v-icon>
          </v-btn>
        </template>
        <v-card >

        </v-card>
      </v-menu>
    </v-toolbar>
    <v-content>
      <v-container>
        <nuxt/>
      </v-container>
    </v-content>
  </v-app>
</template>

<script>
  export default {
    data() {
      return {
        clipped: false,
        drawer: false,
        fixed: false,
        items: [
          {
            icon: 'apps',
            title: 'Welcome',
            to: '/'
          },
          {
            icon: 'bubble_chart',
            title: 'Other',
            to: '/other'
          }
        ],
        miniVariant: false,
        title: 'CCMS'
      }
    }
  }
</script>
