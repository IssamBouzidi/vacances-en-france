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
  <h2>Relation Energie / Intensité :</h2>
  <h4><br>{{resultat}}</h4>
      <img
      src="/images/graph.png" 
      alt=""
      height="480px" 
      width="640px" 
      />

    </main>
  </div>
</div>
% include('scripts.tpl', title='Scripts')
</body>
</html>