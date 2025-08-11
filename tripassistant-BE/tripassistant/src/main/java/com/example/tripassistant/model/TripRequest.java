package com.example.tripassistant.model;

public class TripRequest {
    private String query;
    private int max_cost;

    public String getQuery() {
        return query;
    }

    public void setQuery(String query) {
        this.query = query;
    }

    public int getMax_cost() {
        return max_cost;
    }

    public void setMax_cost(int max_cost) {
        this.max_cost = max_cost;
    }
}
