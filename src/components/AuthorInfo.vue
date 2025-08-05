<template>
	<div>
		<div class="title text-center mt-10">
			<p class="my-2 leading-12" style="font-weight: bolder; font-size: 2.6rem;">{{ mainInfo.title }}</p>
		</div>
		<ul class="author-box mt-8">
			<li v-for="item in mainInfo.authorList" :key="item">
				<a v-if="item.url.trim()!== ''" :href="item.url">{{ item.name }}</a>
				<span v-else>{{ item.name }}</span>
			</li>
		</ul>
		<div class="w-2/5 mx-auto px-4 my-4">
			<ul class="link-box grid grid-cols-1 sm:grid-cols-2 gap-8">
				<li>
					<a href="https://arxiv.org/abs/2209.07753">
						<div><img src="../assets/img/paper_small.png" height="60px"></div>
						<h4><strong>Paper</strong></h4>
					</a>
				</li>
				<li>
					<a href="https://github.com/google-research/google-research/tree/master/code_as_policies">
						<div><img src="../assets/img/github.png" height="60px"></div>
						<h4><strong>Code</strong></h4>
					</a>
				</li>
			</ul>
		</div>
	</div>
</template>

<script setup>
import mainInfo from './../json/mainInfo.json'
</script>
<style>
.author-box li {
	display: inline-block;
	margin: 0 12px 6px;
}

.container a {
	color: #1772d0;
	text-decoration: none;
}

.link-box li div {
	width: 45px;
	height: 60px;
	display: table-cell;
	vertical-align: middle;
	text-align: center;
}
</style>
