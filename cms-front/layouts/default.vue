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
      <v-menu v-model="menu" :close-on-content-click="false" :nudge-width="200" offset-x>
        <template v-slot:activator="{ on }">
          <v-btn fab flat v-on="on">
            <v-icon>person</v-icon>
          </v-btn>
        </template>
        <v-card>
          <v-list>
            <v-list-tile avatar>
              <v-list-tile-avatar>
                <v-icon color="accent">person</v-icon>
              </v-list-tile-avatar>
              <v-list-tile-content>
                <v-list-tile-title>First Last</v-list-tile-title>
              </v-list-tile-content>
            </v-list-tile>
          </v-list>
          <v-divider></v-divider>
          <v-list>
            <v-list-tile>
              <v-list-tile-action>
                <v-switch color="accent"></v-switch>
              </v-list-tile-action>
              <v-list-tile-title>Setting</v-list-tile-title>
            </v-list-tile>
          </v-list>
          <v-card-actions>
            <v-spacer />
            <v-btn flat>Logout</v-btn>
          </v-card-actions>
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
            title: 'Home',
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
