<!doctype html>
<html lang="en">
  <head>
    % include('head.tpl', title='Head')
  </head>
  <body>
  
  % include('top_nav.tpl', title='Top navigation')

<div class="container-fluid">
  <div class="row">
    
	% include('nav.tpl', title='Navigation')

    <main role="main" class="col-md-9 ml-sm-auto col-lg-10 px-md-4">
  <h2>Dur�e moyenne des morceaux</h2>
  <h4><br>La dur�e moyenne des morceaux est de {{tps}} minutes.</h4>
    </main>
  </div>
</div>
% include('scripts.tpl', title='Scripts')
</body>
</html>