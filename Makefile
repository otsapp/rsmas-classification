APP_NAME = "covid_classifier"

Build:
	docker build -t $(APP_NAME) .

Train:
	docker run -t -v /tmp:/tmp $(APP_NAME)

