<template>
  <v-layout>
    <v-flex text-xs-center xs12 offset-xs0 md6 offset-md3>
      <v-card>
        <v-card-title class="headline">Toronto Cat Rescue</v-card-title>
        <v-card-text text-xs-center>
          Central Cat Management System
          <logo />
        </v-card-text>
        <v-card-actions>
          <v-spacer />
          <v-btn color="primary" flat nuxt to="/other">More</v-btn>
        </v-card-actions>
      </v-card>
    </v-flex>
  </v-layout>
</template>

<script>
import Logo from '~/components/Logo.vue'

export default {
  components: {
    Logo
  }
}
</script>
