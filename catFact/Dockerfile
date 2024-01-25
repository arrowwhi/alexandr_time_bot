FROM golang:1.19

WORKDIR /app

COPY src/ .
RUN go mod download

RUN go build -o main .


CMD ["./main"]
