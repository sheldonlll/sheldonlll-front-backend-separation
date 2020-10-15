<template>
	<div class="MusicHome">
	  <v-container>
		
		<!-- 顶部排序 -->
		<v-row dense>
			<v-btn text large>
				<v-icon large>folder</v-icon>
				<span class="caption text-lowercase">By Folder</span>
			</v-btn>
			<v-btn text large>
				<v-icon large>person</v-icon>
				<span class="caption text-lowercase">By Person</span>
			</v-btn>
			<v-btn text large>
				<v-icon large>date_range</v-icon>
				<span class="caption text-lowercase">By Date</span>
			</v-btn>
			<v-spacer></v-spacer>
			<v-btn text large>
				<v-icon large>cloud_upload</v-icon>
				<span class="caption text-lowercase">Upload</span>
			</v-btn>
		</v-row>
		
		<!-- 列表 -->
		<v-row dense>
		  <v-col v-for="card in cards" :key="card.id" :cols="card.flex">
			<v-card depressed>
			  <v-img :src="card.src" class="white--text align-end" gradient="to bottom, rgba(0,0,0,.1), rgba(0,0,0,.5)" height="360px">
				<v-card-title v-text="card.title"></v-card-title>
			  </v-img>
			  <v-card-subtitle class="pb-0">Number 10</v-card-subtitle>
			  <v-card-text class="text--primary">
				  <div>Whitehaven Beach</div>
				  <div>Whitsunday Island, Whitsunday Islands</div>
			  </v-card-text>
			  <v-card-actions>
				<v-spacer></v-spacer>
				<v-btn icon>
				  <v-icon>mdi-heart</v-icon>
				</v-btn>
				<v-btn icon>
				  <v-icon>mdi-bookmark</v-icon>
				</v-btn>
				<v-btn icon>
				  <v-icon>mdi-share-variant</v-icon>
				</v-btn>
			  </v-card-actions>
			</v-card>
		  </v-col>
		</v-row>
	  </v-container>
	</div>
</template>

<script>
  export default {
    data: () => ({
      cards: [
        { id:1, title: 'Pre-fab homes', src: 'https://cdn.vuetifyjs.com/images/cards/docks.jpg', flex: 3 },
        { id:2, title: 'Favorite road trips', src: 'https://cdn.vuetifyjs.com/images/cards/docks.jpg', flex: 3 },
        { id:3, title: 'Best airlines', src: 'https://cdn.vuetifyjs.com/images/cards/docks.jpg', flex: 3 },
		{ id:4, title: 'Pre-fab homes', src: 'https://cdn.vuetifyjs.com/images/cards/docks.jpg', flex: 12 },
		{ id:5, title: 'Favorite road trips', src: 'https://cdn.vuetifyjs.com/images/cards/docks.jpg', flex: 3 },
		{ id:6, title: 'Best airlines', src: 'https://cdn.vuetifyjs.com/images/cards/docks.jpg', flex: 6 },
		{ id:7, title: 'Pre-fab homes', src: 'https://cdn.vuetifyjs.com/images/cards/docks.jpg', flex: 6 },
		{ id:8, title: 'Favorite road trips', src: 'https://cdn.vuetifyjs.com/images/cards/docks.jpg', flex: 3 },
		{ id:9, title: 'Best airlines', src: 'https://cdn.vuetifyjs.com/images/cards/docks.jpg', flex: 3 },
		{ id:10, title: 'Pre-fab homes', src: 'https://cdn.vuetifyjs.com/images/cards/docks.jpg', flex: 4 },
		{ id:11, title: 'Favorite road trips', src: 'https://cdn.vuetifyjs.com/images/cards/docks.jpg', flex: 3 },
		{ id:12, title: 'Best airlines', src: 'https://cdn.vuetifyjs.com/images/cards/docks.jpg', flex: 4 },
		{ id:13, title: 'Pre-fab homes', src: 'https://cdn.vuetifyjs.com/images/cards/docks.jpg', flex: 3 },
		{ id:14, title: 'Favorite road trips', src: 'https://cdn.vuetifyjs.com/images/cards/docks.jpg', flex: 3 },
		{ id:15, title: 'Best airlines', src: 'https://cdn.vuetifyjs.com/images/cards/docks.jpg', flex: 4 },
      ],
    }),
	created(){
		// 整理布局
		this.cards.sort((a,b)=>{return a.flex > b.flex ? -1:1})
	},
	components:{
	}
  }
</script>

<style>
</style>
