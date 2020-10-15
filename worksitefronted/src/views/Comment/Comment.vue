<template>
	<v-container>
		<v-row>
			<v-col cols='12'>
				<div class="biu">
					<BiuBox :ContentType="ContentType" :ObjectId="ObjectId"></BiuBox>
				</div>
				<br><hr class="cutline"><br>
				<div class="commentlist">
					<BiuList :ContentType="ContentType" :ObjectId="ObjectId"></BiuList>
				</div>
			</v-col>
		</v-row>
    </v-container>
</template>
<script>
	import {getcomment} from '@/network/Comment/Comment.js'
	import BiuBox from '@/views/Comment/BiuBox.vue'
	import BiuList from '@/views/Comment/BiuList.vue'
	export default{
		data(){
			return{

			}
		},
		components:{
			BiuBox,
			BiuList
		},
		props:{
			ContentType:{
				type:Number,
				default:null
			},
			ObjectId:{
				type:Number,
				default:null
			}
		},
	}
</script>

<style scoped="scoped">
	.cutline{
		border: 1px dotted #BABABA;
	}
</style>
