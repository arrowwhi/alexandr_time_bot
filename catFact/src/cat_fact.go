package main

import (
	"github.com/PuerkitoBio/goquery"
	"log"
	"math/rand"
	"net/http"
	"strings"
	"time"
)

func GetFact() string {
	once.Do(func() {
		arr = GetAllFacts()
	})

	rand.Seed(time.Now().UnixNano())
	return arr[rand.Intn(len(arr))]
}

func GetAllFacts() []string {
	res, err := http.Get("https://100-faktov.ru/o-koshkax/")
	if err != nil {
		log.Fatal(err)
	}
	defer res.Body.Close()
	if res.StatusCode != 200 {
		log.Fatalf("status code error: %d %s", res.StatusCode, res.Status)
	}

	// Load the HTML document
	doc, err := goquery.NewDocumentFromReader(res.Body)
	if err != nil {
		log.Fatal(err)
	}

	// Find items
	var sol []string
	doc.Find(".entry-content").Find("p").Each(func(i int, s *goquery.Selection) {
		sol = append(sol, strings.Split(s.Text(), ".")[1])
	})

	return sol[2:]
}
