package com.example.tripassistant.controller;
import com.example.tripassistant.model.TripRequest;
import org.springframework.http.*;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.client.RestTemplate;

import java.util.Map;

@RestController
@RequestMapping("/api")
@CrossOrigin(origins = "*")
public class TripController {
    @PostMapping("/request-trip")
    public ResponseEntity<?> requestTrip(@RequestBody TripRequest request) {
        try {
            RestTemplate restTemplate = new RestTemplate();
            String fastApiUrl = "http://localhost:8000/suggest";  // URL của FastAPI

            HttpHeaders headers = new HttpHeaders();
            headers.setContentType(MediaType.APPLICATION_JSON);

            HttpEntity<TripRequest> entity = new HttpEntity<>(request, headers);
            ResponseEntity<Object> response = restTemplate.exchange(fastApiUrl, HttpMethod.POST, entity, Object.class);

            return ResponseEntity.ok(response.getBody());
        } catch (Exception e) {
            return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR)
                    .body(Map.of("error", "Lỗi khi gọi AI API", "details", e.getMessage()));
        }
    }

}
