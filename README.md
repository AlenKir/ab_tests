﻿# A simple **REST API** for managing A/B testing
Ensures that devices consistently receive the same experiment assignments and excludes existing devices from new experiments.

- **Device-Specific Experiment Assignments**  
  - Each device receives a unique, consistent experiment assignment.  
- **Probability-Based Experiment Distribution**  
  - Ensures correct distribution of test groups based on predefined probabilities.  
- **Exclusion of Existing Devices from New Experiments**  
  - Only new devices participate in newly created experiments.  
- **Experiment Statistics Dashboard**  
  - Displays total devices per experiment and option distribution.

## API Endpoints  

### GET /experiments  
Retrieve assigned experiments for a device.  

#### Request Headers:  
```http
Device-Token: device_123
```

#### Response example:  
```http
{
    "button_color": "#FF0000",
    "price": 10
}
![photo_2025-02-10_13-47-01](https://github.com/user-attachments/assets/8ff3dbd9-c152-4522-8486-4030fb05a828)
![image](https://github.com/user-attachments/assets/acd72cab-82f5-4ee4-b6d8-07ef3042dd76)
