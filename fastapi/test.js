import http from 'k6/http';

export const options = {
    vus: 200,  // 10 virtual users
    // duration: '10s',  // Run for 30 seconds
    iterations: 200
};

export default function () {
    const BASE_URL = 'http://localhost:8003';
    const globalStartTime = new Date().getTime();

    const requests = [
        // ...Array(10).fill({ 
        //     method: 'GET', 
        //     url: `${BASE_URL}/test`,
        //     tags: { name: 'test_endpoint' }
        // }),
        { 
            method: 'GET', 
            url: `${BASE_URL}/`,
            tags: { name: 'root_endpoint' }
        }
    ];

    const responses = http.batch(requests);

    responses.forEach((res, index) => {
        const requestStartTime = res.timings.blocked + res.timings.connecting + res.timings.tls_handshaking + res.timings.sending;
        const requestEndTime = requestStartTime + res.timings.waiting + res.timings.receiving;
        
        console.log(`VU ${__VU} - Request ${index + 1}:
            Started at: ${requestStartTime/1000}s
            Actual completion: ${requestEndTime/1000}s
            Request Duration: ${res.timings.duration}ms
            URL: ${res.request.url}
            Response: ${res.body}
        `);
    });
}
