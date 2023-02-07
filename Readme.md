docker run --network fast-network -dp 8000:8000 --name fast-code --mount type=bind,src="$(pwd)/app",target=/code/app fast-api

docker run --network fast-network -dp 3308:3306 -v /database:/var/lib/mysql -e MYSQL_ROOT_PASSWORD=secret -e MYSQL_DATABASE=db --name fast-database mysql:8.0