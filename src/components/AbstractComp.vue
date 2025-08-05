<template>
	<div class="mt-4">
		<video id="v0" width="100%" preload="metadata" playsinline="" muted="" loop="" autoplay="">
			<source :src="mainInfo.mainGif" type="video/mp4">
		</video>
		<div class="mt-4 text-left">
			<h1 class="text-2xl leading-20">Abstract</h1>
			<p class="text-base leading-6">
				{{ mainInfo.abstract }}</p>
			<p class="mt-4 text-center">
				<img src="../assets/img/share_image.png" width="100%">
			</p>
			<div class="mt-8">
				<video id="v0" width="100%" preload="metadata" playsinline="" controls="">
					<source :src="mainInfo.mainVideo" type="video/mp4">
				</video>
			</div>
			<div class="mt-8 text-left">
				<h3 class="text-2xl leading-20">Experiment Videos and Generated Code</h3>
				<p class="mt-2 text-base leading-6">Videos have sound that showcase voice and speech-based robot
					interface.</p>
				<p class="mt-6 text-base leading-6">Long pauses between commands and responses are mostly caused by
					OpenAI API query times and rate limiting.</p>
			</div>
		</div>
	</div>
</template>

<script setup>
import mainInfo from './../json/mainInfo.json'
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped></style>
