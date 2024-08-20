# Ensure the Nginx package is installed
package { 'nginx':
  ensure => 'installed',
}

# Ensure the default Nginx configuration file is present
file { '/etc/nginx/sites-available/default':
  ensure  => file,
  content => '
    server {
        listen 80 default_server;
        listen [::]:80 default_server;

        root /var/www/html;
        index index.html index.htm;

        server_name _;

        # Redirect /redirect_me to YouTube
        location /redirect_me {
            rewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;
        }

        # Custom 404 error page
        location = /404.html {
            internal;
        }

        # Handle root requests
        location / {
            try_files $uri $uri/ =404;
        }
    }
  ',
  notify  => Service['nginx'],
}

# Ensure the index.html file is present
file { '/var/www/html/index.html':
  ensure  => file,
  content => 'Hello World!',
}

# Ensure the Nginx service is running
service { 'nginx':
  ensure    => running,
  subscribe => File['/etc/nginx/sites-available/default'],
}
