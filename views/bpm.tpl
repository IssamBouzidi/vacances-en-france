<!doctype html>
<html lang="en">
  <head>
    % include('head.tpl', title='Head')
  </head>
  <body>
	
<div class="container-fluid">
  <div class="row">
    
	% include('nav.tpl', title='Navigation')

    <main role="main" class="col-md-9 ml-sm-auto col-lg-10 px-md-4">
      
      <h2>Nombre de titres par BPM</h2>
	  
      <div class="table-responsive">
        <table class="table table-striped table-sm">
          <thead>
            <tr>
              <th>Nombre de titres</th>
              <th>Intervalle de BPM</th>
            </tr>
          </thead>
          <tbody>
		  %for row in rows:
            <tr>
              %for col in row:
				<td>{{col}}</td>
				%end
            </tr>
			%end
          </tbody>
        </table>
      </div>
    </main>
  </div>
</div>
	% include('scripts.tpl', title='Scripts')
	</body>
</html>