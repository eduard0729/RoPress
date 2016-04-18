<?php
$servername = "104.238.188.243";
$username = "admin_press";
$password = "tekit2016";
$dbname = "admin_press";
$conn = new mysqli($servername, $username, $password, $dbname);
// Check connection
if ($conn->connect_error) {
     die("Connection failed: " . $conn->connect_error);
} 
header('Content-Type: text/html; charset=utf-8');
?>
<!DOCTYPE html>
<html lang="en" class="no-js">
	<head>
		<meta charset="UTF-8">
		<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
		<meta http-equiv="X-UA-Compatible" content="IE=edge">
		<meta name="viewport" content="width=device-width, initial-scale=1">
		<title>RoPress</title>
		<meta name="description" content="Some animation ideas for stacks of cards" />
		<meta name="keywords" content="stack, cards, effect, ui, animation, inspiration, html, css" />
		<meta name="author" content="Codrops" />
		<link rel="shortcut icon" href="favicon.ico">
		<link rel="stylesheet" type="text/css" href="css/normalize.css" />
		<link rel="stylesheet" type="text/css" href="fonts/font-awesome-4.3.0/css/font-awesome.min.css" />
		<link rel="stylesheet" type="text/css" href="css/demo.css" />
		<link rel="stylesheet" type="text/css" href="css/component.css" />
		<script src="js/modernizr-custom.js"></script>
	</head>
	<body>
		<div class="container">
			<header class="codrops-header color-0">
				<img src="img/sigla.png">
			</header>
			<div class="content color-5">
				<h2 class="content__title">RoPress</h2>
				<div class="counter" id="counter">
					<svg width="40" height="40" viewBox="0 0 60 60">
						<path d="M55.215 8.397c-0.336-1.32-1.968-2.397-3.63-2.397h-43.17c-1.665 0-3.297 1.077-3.63 2.397l-0.603 3.603h51.633l-0.6-3.603zM58.236 15h-56.475c-1.026 0-1.827 0.882-1.731 1.905l2.769 35.007c0.114 1.182 1.11 2.088 2.298 2.088h49.803c1.191 0 2.184-0.906 2.298-2.088l2.769-35.007c0.099-1.023-0.705-1.905-1.731-1.905zM37.314 25.125c1.554 0 2.814 1.26 2.814 2.814s-1.26 2.814-2.814 2.814-2.814-1.263-2.814-2.817c0-1.551 1.26-2.811 2.814-2.811zM16.5 42l7.458-17.142 8.481 13.728 7.272-3.612 3.789 7.026h-27z"></path>
					</svg>
					<span class="text-hidden">Saved Images</span>
					<span class="counter__number">0</span>
				</div>
				<ul id="stack_slamet" class="stack stack--slamet">
					<?php

					$sql = "SELECT title, press, textul, county FROM press order by id desc limit 50";
					$conn->query("SET CHARACTER SET utf8");
					$conn->query("SET NAMES utf8");
					$result = $conn->query($sql);
					if (mysqli_num_rows($result) > 0) {
    // output data of each row
    				while($row = mysqli_fetch_assoc($result)) {
        				echo '<li class="stack__item">';
        				echo '<h3>'.$row["title"].'</h3>';
        				echo '<p>Ziar: <em>' . $row["press"]. '</em></p>'; 
        				echo '<p><em>' . $row["county"]. '</em></p>'; 
        				echo '<p>' . $row["textul"] . '</p>';
        				echo '</li>';
    				}
					} else {
    					echo "0 results";
					}

					mysqli_close($conn);
					?>
				</ul>
				<div class="controls">
					<button class="button button--sonar button--reject" data-stack="stack_slamet"><i class="fa fa-times"></i><span class="text-hidden">Reject</span></button>
					<button class="button button--sonar button--accept" data-stack="stack_slamet"><i class="fa fa-check"></i><span class="text-hidden">Accept</span></button>
				</div>
			</div>
			<!-- Related demos -->
		</div><!-- /container -->
		<script src="js/classie.js"></script>
		<!--
		click feedback effect : see more at http://tympanus.net/codrops/2015/02/11/subtle-click-feedback-effects/
		-->
		<script>
			// http://stackoverflow.com/a/11381730/989439
			function mobilecheck() {
				var check = false;
				(function(a){if(/(android|ipad|playbook|silk|bb\d+|meego).+mobile|avantgo|bada\/|blackberry|blazer|compal|elaine|fennec|hiptop|iemobile|ip(hone|od)|iris|kindle|lge |maemo|midp|mmp|netfront|opera m(ob|in)i|palm( os)?|phone|p(ixi|re)\/|plucker|pocket|psp|series(4|6)0|symbian|treo|up\.(browser|link)|vodafone|wap|windows (ce|phone)|xda|xiino/i.test(a)||/1207|6310|6590|3gso|4thp|50[1-6]i|770s|802s|a wa|abac|ac(er|oo|s\-)|ai(ko|rn)|al(av|ca|co)|amoi|an(ex|ny|yw)|aptu|ar(ch|go)|as(te|us)|attw|au(di|\-m|r |s )|avan|be(ck|ll|nq)|bi(lb|rd)|bl(ac|az)|br(e|v)w|bumb|bw\-(n|u)|c55\/|capi|ccwa|cdm\-|cell|chtm|cldc|cmd\-|co(mp|nd)|craw|da(it|ll|ng)|dbte|dc\-s|devi|dica|dmob|do(c|p)o|ds(12|\-d)|el(49|ai)|em(l2|ul)|er(ic|k0)|esl8|ez([4-7]0|os|wa|ze)|fetc|fly(\-|_)|g1 u|g560|gene|gf\-5|g\-mo|go(\.w|od)|gr(ad|un)|haie|hcit|hd\-(m|p|t)|hei\-|hi(pt|ta)|hp( i|ip)|hs\-c|ht(c(\-| |_|a|g|p|s|t)|tp)|hu(aw|tc)|i\-(20|go|ma)|i230|iac( |\-|\/)|ibro|idea|ig01|ikom|im1k|inno|ipaq|iris|ja(t|v)a|jbro|jemu|jigs|kddi|keji|kgt( |\/)|klon|kpt |kwc\-|kyo(c|k)|le(no|xi)|lg( g|\/(k|l|u)|50|54|\-[a-w])|libw|lynx|m1\-w|m3ga|m50\/|ma(te|ui|xo)|mc(01|21|ca)|m\-cr|me(rc|ri)|mi(o8|oa|ts)|mmef|mo(01|02|bi|de|do|t(\-| |o|v)|zz)|mt(50|p1|v )|mwbp|mywa|n10[0-2]|n20[2-3]|n30(0|2)|n50(0|2|5)|n7(0(0|1)|10)|ne((c|m)\-|on|tf|wf|wg|wt)|nok(6|i)|nzph|o2im|op(ti|wv)|oran|owg1|p800|pan(a|d|t)|pdxg|pg(13|\-([1-8]|c))|phil|pire|pl(ay|uc)|pn\-2|po(ck|rt|se)|prox|psio|pt\-g|qa\-a|qc(07|12|21|32|60|\-[2-7]|i\-)|qtek|r380|r600|raks|rim9|ro(ve|zo)|s55\/|sa(ge|ma|mm|ms|ny|va)|sc(01|h\-|oo|p\-)|sdk\/|se(c(\-|0|1)|47|mc|nd|ri)|sgh\-|shar|sie(\-|m)|sk\-0|sl(45|id)|sm(al|ar|b3|it|t5)|so(ft|ny)|sp(01|h\-|v\-|v )|sy(01|mb)|t2(18|50)|t6(00|10|18)|ta(gt|lk)|tcl\-|tdg\-|tel(i|m)|tim\-|t\-mo|to(pl|sh)|ts(70|m\-|m3|m5)|tx\-9|up(\.b|g1|si)|utst|v400|v750|veri|vi(rg|te)|vk(40|5[0-3]|\-v)|vm40|voda|vulc|vx(52|53|60|61|70|80|81|83|85|98)|w3c(\-| )|webc|whit|wi(g |nc|nw)|wmlb|wonu|x700|yas\-|your|zeto|zte\-/i.test(a.substr(0,4)))check = true})(navigator.userAgent||navigator.vendor||window.opera);
				return check;
			}

			var clickeventtype = mobilecheck() ? 'touchstart' : 'click';

			(function() {
				var support = { animations : Modernizr.cssanimations },
					animEndEventNames = { 'WebkitAnimation' : 'webkitAnimationEnd', 'OAnimation' : 'oAnimationEnd', 'msAnimation' : 'MSAnimationEnd', 'animation' : 'animationend' },
					animEndEventName = animEndEventNames[ Modernizr.prefixed( 'animation' ) ],
					onEndAnimation = function( el, callback ) {
						var onEndCallbackFn = function( ev ) {
							if( support.animations ) {
								if(ev.target != this) return;
								this.removeEventListener( animEndEventName, onEndCallbackFn);
							}
							if(callback && typeof callback === 'function') {callback.call();}
						};
						if( support.animations ) {
							el.addEventListener(animEndEventName, onEndCallbackFn);
						}
						else {
							onEndCallbackFn();
						}
					};

				[].slice.call(document.querySelectorAll('.button--sonar')).forEach(function(el) {
					el.addEventListener(clickeventtype, function(ev) {
						if( el.getAttribute('data-state') !== 'locked' ) {
							classie.add(el, 'button--active');
							onEndAnimation(el, function() {
								classie.remove(el, 'button--active');
							});
						}
					});
				});
			})();
		</script>
		<script src="js/dynamics.min.js"></script>
		<script src="js/main.js"></script>
		<script>
			(function() {
				
				var support = { animations : Modernizr.cssanimations },
					animEndEventNames = { 'WebkitAnimation' : 'webkitAnimationEnd', 'OAnimation' : 'oAnimationEnd', 'msAnimation' : 'MSAnimationEnd', 'animation' : 'animationend' },
					animEndEventName = animEndEventNames[ Modernizr.prefixed( 'animation' ) ],
					onEndAnimation = function( el, callback ) {
						var onEndCallbackFn = function( ev ) {
							if( support.animations ) {
								if(ev.target != this) return;
								this.removeEventListener( animEndEventName, onEndCallbackFn);
							}
							if(callback && typeof callback === 'function') {callback.call();}
						};
						if( support.animations ) {
							el.addEventListener(animEndEventName, onEndCallbackFn);
						}
						else {
							onEndCallbackFn();
						}
					};

				function nextSibling(el) {
					var nextSibling = el.nextSibling;
					while(nextSibling && nextSibling.nodeType != 1) {
					nextSibling = nextSibling.nextSibling
					}
					return nextSibling;
				}

				var slamet = new Stack(document.getElementById('stack_slamet'), {
						infinite: false,
						perspective: 1400,
						onEndStack: function(instance) {
							setTimeout(function() {
								instance.restart();
								document.querySelector('#counter > .counter__number').innerHTML = 0;
							}, 300);
						}
					});

				// controls the click ring effect on the button
				var buttonClickCallback = function(bttn) {
					var bttn = bttn || this;
					bttn.setAttribute('data-state', 'unlocked');
				};

				document.querySelector('.button--accept[data-stack = stack_slamet]').addEventListener(clickeventtype, function(ev) { 
					var callback = function() {
						// increment counter
						var counter = document.querySelector('#counter > .counter__number'),
							count = parseInt(counter.innerHTML);
						counter.innerHTML = count + 1;

						buttonClickCallback(ev.target);
					};
					slamet.accept(callback);
				});
				document.querySelector('.button--reject[data-stack = stack_slamet]').addEventListener(clickeventtype, function() { slamet.reject(buttonClickCallback.bind(this)); });	

				[].slice.call(document.querySelectorAll('.button--sonar')).forEach(function(bttn) {
					bttn.addEventListener(clickeventtype, function() {
						bttn.setAttribute('data-state', 'locked');
					});
				});

				[].slice.call(document.querySelectorAll('.button--material')).forEach(function(bttn) {
					var radialAction = nextSibling(bttn.parentNode);

					bttn.addEventListener(clickeventtype, function(ev) {
						var boxOffset = radialAction.parentNode.getBoundingClientRect(),
							offset = bttn.getBoundingClientRect();

						radialAction.style.left = Number(offset.left - boxOffset.left) + 'px';
						radialAction.style.top = Number(offset.top - boxOffset.top) + 'px';

						classie.add(radialAction, classie.has(bttn, 'button--reject') ? 'material-circle--reject' : 'material-circle--accept');
						classie.add(radialAction, 'material-circle--active');
						onEndAnimation(radialAction, function() {
							classie.remove(radialAction, classie.has(bttn, 'button--reject') ? 'material-circle--reject' : 'material-circle--accept');
							classie.remove(radialAction, 'material-circle--active');
						});
					});
				});
			})();
		</script>
	</body>
</html>
