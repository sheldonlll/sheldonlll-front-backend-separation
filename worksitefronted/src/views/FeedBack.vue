<template>
	<div class="FeedBack">
	  <v-container>
		<!-- 列表 -->
		<v-row dense>
			<v-btn text large>
				<v-icon large>chat</v-icon>
				<span class="caption text-lowercase">Leave A Message</span>
			</v-btn>
		</v-row>
		<v-row dense>
		  <v-col v-for="card in cards" :key="card.id" :cols="card.flex">
			<v-card  elevation="3">
			  <v-card-text class="text--primary">
				  <div>Whitehaven Beach</div>
				  <div>Whitsunday Island, Whitsunday Islands</div>
			  </v-card-text>
			  <v-expand-transition>
			    <div v-show="show">
			  	<v-divider></v-divider>
			  		
			  	<v-card-text>
			  	  I'm a thing. But, like most politicians, he promised more than he could deliver. You won't have time for sleeping, soldier, not with all the bed making you'll be doing. Then we'll go with that data file! Hey, you add a one and two zeros to that or we walk! You're going to do his laundry? I've got to find a way to escape.
			  	</v-card-text>
			    </div>
			  </v-expand-transition>
			</v-card>

		  </v-col>
		</v-row>
	  </v-container>
	</div>
</template>

<script>
  export default {
    data: () => ({
	  show: false,
      cards: [
        { id:1, title: 'Pre-fab homes', src: 'https://cdn.vuetifyjs.com/images/cards/docks.jpg', flex: 3 },
        { id:2, title: 'Favorite road trips', src: 'https://cdn.vuetifyjs.com/images/cards/docks.jpg', flex: 3 },
        { id:3, title: 'Best airlines', src: 'https://cdn.vuetifyjs.com/images/cards/docks.jpg', flex: 3 },
		{ id:6, title: 'Best airlines', src: 'https://cdn.vuetifyjs.com/images/cards/docks.jpg', flex: 6 },
		{ id:9, title: 'Best airlines', src: 'https://cdn.vuetifyjs.com/images/cards/docks.jpg', flex: 3 },
		{ id:12, title: 'Best airlines', src: 'https://cdn.vuetifyjs.com/images/cards/docks.jpg', flex: 4 },
		{ id:3, title: 'Best airlines', src: 'https://cdn.vuetifyjs.com/images/cards/docks.jpg', flex: 3 },
		{ id:13, title: 'Pre-fab homes', src: 'https://cdn.vuetifyjs.com/images/cards/docks.jpg', flex: 3 },
		{ id:6, title: 'Best airlines', src: 'https://cdn.vuetifyjs.com/images/cards/docks.jpg', flex: 6 },
		{ id:6, title: 'Best airlines', src: 'https://cdn.vuetifyjs.com/images/cards/docks.jpg', flex: 6 },
		{ id:12, title: 'Best airlines', src: 'https://cdn.vuetifyjs.com/images/cards/docks.jpg', flex: 4 },
      ],
    }),
	created(){
		// 整理布局
		this.cards.sort((a,b)=>{return a.flex > b.flex ? -1:1})
	}
  }
</script>

<style>
</style>
