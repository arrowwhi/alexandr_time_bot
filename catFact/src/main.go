package main

import (
	"context"
	"google.golang.org/grpc"
	"log"
	"net"
	"sync"

	pb "catFact/cat_fact"
)

var (
	once sync.Once
	arr  []string
)

type server struct {
	pb.UnimplementedCatFactServiceServer
}

func (s *server) GetResponse(ctx context.Context, request *pb.EmptyRequest) (*pb.Response, error) {
	return &pb.Response{Message: GetFact()}, nil
}

func main() {
	listener, err := net.Listen("tcp", ":50051")
	if err != nil {
		log.Fatalf("failed to listen: %v", err)
	}

	srv := grpc.NewServer()
	pb.RegisterCatFactServiceServer(srv, &server{})

	log.Println("Server is running on :50051")
	if err := srv.Serve(listener); err != nil {
		log.Fatalf("failed to serve: %v", err)
	}
}
