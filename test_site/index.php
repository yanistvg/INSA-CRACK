<!DOCTYPE html>
<html>
<head>
	<title>Posts</title>
	<link rel="stylesheet" type="text/css" href="./all.css">
</head>
<body>
<body ng-app="blogApp">
  
  <div ng-controller="BlogController as blog">
      <div class="topbar">
        <div class="container">
          <div class="row">
            <div class="col-s-4">
              <h1 ng-click="blog.selectTab('blog')" class="push-left">Super Secure Blog</h1>
            </div>
            <div class="offset-s-4 col-s-4">
              <nav role='navigation' class="push-right">
                <ul>
                  <li><a href="#" ng-click="blog.selectTab('blog')">See All Posts</a></li> //
                  <li><a href="#" ng-click="blog.selectTab('new')">Add New Post</a></li>
                </ul>
              </nav> 
            </div>
          </div>
        </div>
        
        
         
      </div>
     
      
      <div class="content">
        <div class="container">
          <div class="row">
            <ul class="post-grid" ng-show="blog.isSelected('blog')">
          <li ng-repeat="post in blog.posts" class="col-s-4" ng-class="{ 'reset-s' : $index%3==0 }" ng-click="blog.selectTab($index)" >
            <h3>New Update</h3>
            <p>Just get  the first user on the blog. I removed my first post for security resons.</p>
          </li>
        </ul>
        <div class="post" ng-repeat="post in blog.posts" ng-show="blog.isSelected($index)">
          <div>
            
            <h2>Still no one here </h2>
            <img src="{{post.image}}" ng-show="{{post.image}}"/>
            <cite>by admin on 12/12/12</cite>
            <div class="post-body">
             <p ng-repeat="paragraph in post.body">
               Not having success yet. But Roma wasn't built in one day.
             </p> 
            </div>
            
            
        <div class="post" ng-show="blog.isSelected('new')">
          <h2>Add New Post</h2>
          
          <form name="postForm" ng-submit=" blog.addPost()" novalidate>
                  <h4>Title</h4>
                  <input type="text" ng-model="blog.post.title"/>
                  <h4>Body</h4>
                  <textarea ng-model="blog.post.body" ng-list="/\n/" rows="10"></textarea>
                  <label for="">Featured Image URL</label>
                  <input type="text" ng-model="blog.post.image" placeholder="https://isi.insa-cvl.fr" />
                  <label for="">by:</label>
                  <input type="text" ng-model="blog.post.author" placeholder="Author Name" required/>
                  
                  <input type="submit" value="Submit" />
                </select></form>
          
            </div>
            
          </div>
        </div>
        
    </div>
  </div>
  
  
</body>
</body>
</html>