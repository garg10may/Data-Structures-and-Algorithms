import http from 'k6/http';

export default function () {
    const BASE_URL = 'localhost:8003'; 

    // Create the requests
    const requests = [
        ...Array(10).fill({ method: 'GET', url: `${BASE_URL}/test` }), // 10 requests to /test
        { method: 'GET', url: `${BASE_URL}/` },                       // 1 request to /
        { method: 'GET', url: `${BASE_URL}/count` }                   // 1 request to /count
    ];

    // Execute the requests in parallel
    const responses = http.batch(requests);

    // Optional: Log response statuses for debugging
    responses.forEach((res, index) => {
        console.log(`Request ${index + 1}: ${res.status}`);
    });
}
