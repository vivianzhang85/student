/**
 * NYC Landmarks API Configuration
 * College Board Create PT Compliant
 * Shows: Input/Output, Procedures, Logic
 */

// API Configuration
const API_CONFIG = {
    pythonURI: "http://localhost:5000",
    fetchOptions: {
        mode: 'cors',
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        }
    },
    
    // Museum mapping
    museums: {
        'met-section': 'met',
        'icecream-section': 'icecream',
        'empire-section': 'empire',
        'ukrainian-section': 'ukrainian'
    },
    
    // Landmark details for itinerary
    landmarkDetails: {
        'The Metropolitan Museum of Art': {
            id: 'met',
            location: 'Upper East Side',
            hours: '10:00 AM - 5:30 PM',
            price: '$30 (Adults)',
            type: 'museum'
        },
        'Museum of Ice Cream': {
            id: 'icecream',
            location: 'Soho',
            hours: '10:00 AM - 8:00 PM',
            price: '$39 (All Ages)',
            type: 'interactive'
        },
        'Empire State Building': {
            id: 'empire',
            location: 'Midtown',
            hours: '8:00 AM - 2:00 AM',
            price: '$44 (Adults)',
            type: 'landmark'
        },
        'Ukrainian Museum': {
            id: 'ukrainian',
            location: 'East Village',
            hours: '11:30 AM - 5:00 PM',
            price: '$12 (Adults)',
            type: 'cultural'
        }
    },
    
    // Procedures for API interactions
    procedures: {
        
        /**
         * Procedure 1: Save Landmark to Itinerary
         * Demonstrates: Input processing, API call, Output handling
         */
        async saveLandmarkToItinerary(landmarkName) {
            console.log(`Procedure: Saving ${landmarkName} to itinerary`);
            
            // INPUT: Get landmark details
            const details = this.landmarkDetails[landmarkName];
            if (!details) {
                return {
                    success: false,
                    error: `Unknown landmark: ${landmarkName}`
                };
            }
            
            // Prepare request data
            const landmarkData = {
                name: landmarkName,
                ...details,
                selected_at: new Date().toISOString()
            };
            
            try {
                // API CALL: POST request to backend
                const response = await fetch(`${this.pythonURI}/api/itinerary/section/landmarks`, {
                    ...this.fetchOptions,
                    method: 'POST',
                    body: JSON.stringify(landmarkData)
                });
                
                const data = await response.json();
                
                // OUTPUT: Handle response
                if (data.success) {
                    console.log(`✓ Added ${landmarkName} to itinerary`);
                    return {
                        success: true,
                        message: `Added ${landmarkName} to your itinerary`,
                        data: data.data
                    };
                } else {
                    return {
                        success: false,
                        error: data.message || 'Failed to save landmark'
                    };
                }
            } catch (error) {
                console.error('Procedure error:', error);
                return {
                    success: false,
                    error: 'Network error. Please check your connection.'
                };
            }
        },
        
        /**
         * Procedure 2: Fetch Live Museum Hours
         * Demonstrates: API call, Data processing, Error handling
         */
        async fetchMuseumHours(museumId) {
            console.log(`Procedure: Fetching hours for ${museumId}`);
            
            const museumKey = this.museums[museumId];
            if (!museumKey) {
                return {
                    success: false,
                    error: `Invalid museum section: ${museumId}`
                };
            }
            
            try {
                // API CALL: GET request for museum data
                const response = await fetch(
                    `${this.pythonURI}/api/${museumKey}`,
                    { ...this.fetchOptions, method: 'GET' }
                );
                
                const data = await response.json();
                
                // PROCESS data
                if (data.success) {
                    const museumData = data.data;
                    
                    // Format hours for display
                    const formattedHours = this.formatHoursForDisplay(museumData.hours);
                    
                    // OUTPUT: Return processed data
                    return {
                        success: true,
                        data: {
                            ...museumData,
                            formatted_hours: formattedHours,
                            display_status: this.getStatusDisplay(museumData.status)
                        }
                    };
                } else {
                    return {
                        success: false,
                        error: data.error || 'Failed to fetch hours'
                    };
                }
            } catch (error) {
                console.error('Procedure error:', error);
                return {
                    success: false,
                    error: 'Unable to fetch live hours'
                };
            }
        },
        
        /**
         * Procedure 3: Get Complete Itinerary
         * Demonstrates: Data retrieval, State management
         */
        async getCompleteItinerary() {
            console.log('Procedure: Getting complete itinerary');
            
            try {
                // API CALL: GET request for itinerary
                const response = await fetch(
                    `${this.pythonURI}/api/itinerary`,
                    { ...this.fetchOptions, method: 'GET' }
                );
                
                const data = await response.json();
                
                // PROCESS: Calculate statistics
                if (data.success) {
                    const itinerary = data.data;
                    const stats = this.calculateItineraryStats(itinerary);
                    
                    // OUTPUT: Return combined data
                    return {
                        success: true,
                        data: itinerary,
                        statistics: stats
                    };
                } else {
                    return {
                        success: false,
                        error: 'Failed to retrieve itinerary'
                    };
                }
            } catch (error) {
                console.error('Procedure error:', error);
                return {
                    success: false,
                    error: 'Unable to load itinerary'
                };
            }
        },
        
        /**
         * Procedure 4: Calculate Optimal Schedule
         * Demonstrates: Algorithm implementation, Data processing
         */
        async calculateOptimalSchedule(selectedLandmarks, tripDays) {
            console.log('Procedure: Calculating optimal schedule');
            
            // INPUT validation
            if (!selectedLandmarks || selectedLandmarks.length === 0) {
                return {
                    success: false,
                    error: 'No landmarks selected'
                };
            }
            
            // Prepare request data
            const scheduleData = {
                landmarks: selectedLandmarks.map(name => ({
                    name: name,
                    id: this.landmarkDetails[name]?.id
                })),
                trip_days: tripDays || ['Friday', 'Saturday', 'Sunday']
            };
            
            try {
                // API CALL: POST request for schedule calculation
                const response = await fetch(`${this.pythonURI}/api/calculate-schedule`, {
                    ...this.fetchOptions,
                    method: 'POST',
                    body: JSON.stringify(scheduleData)
                });
                
                const data = await response.json();
                
                // PROCESS: Format schedule output
                if (data.success) {
                    const formattedSchedule = this.formatScheduleForDisplay(data.data.schedule);
                    
                    // OUTPUT: Return calculated schedule
                    return {
                        success: true,
                        data: data.data,
                        formatted_schedule: formattedSchedule,
                        recommendations: this.generateRecommendations(data.data)
                    };
                } else {
                    return {
                        success: false,
                        error: data.error || 'Schedule calculation failed'
                    };
                }
            } catch (error) {
                console.error('Procedure error:', error);
                return {
                    success: false,
                    error: 'Unable to calculate schedule'
                };
            }
        },
        
        // Helper functions
        formatHoursForDisplay(hours) {
            if (typeof hours === 'string') return hours;
            
            let formatted = '';
            for (const [day, time] of Object.entries(hours)) {
                formatted += `${day}: ${time}\n`;
            }
            return formatted.trim();
        },
        
        getStatusDisplay(status) {
            const lowerStatus = status.toLowerCase();
            if (lowerStatus.includes('open')) {
                return '<span class="status-open">OPEN</span>';
            } else if (lowerStatus.includes('closed')) {
                return '<span class="status-closed">CLOSED</span>';
            }
            return status;
        },
        
        calculateItineraryStats(itinerary) {
            const landmarkCount = itinerary.landmarks?.length || 0;
            const types = new Set();
            
            itinerary.landmarks?.forEach(landmark => {
                types.add(landmark.type || 'unknown');
            });
            
            return {
                total_landmarks: landmarkCount,
                types_count: types.size,
                types: Array.from(types),
                last_updated: itinerary.landmarks?.[landmarkCount - 1]?.selected_at || 'Never'
            };
        },
        
        formatScheduleForDisplay(schedule) {
            return schedule.map(day => ({
                day: day.day,
                activities: day.landmarks.map(l => `${l.name} (${l.hours})`)
            }));
        },
        
        generateRecommendations(scheduleData) {
            const recommendations = [];
            
            if (scheduleData.total_landmarks > 3) {
                recommendations.push('Consider spreading visits across multiple days');
            }
            
            if (scheduleData.days_planned > 0) {
                recommendations.push(`Plan ${scheduleData.total_landmarks} landmark visits`);
            }
            
            return recommendations;
        }
    }
};

// Export configuration
export default API_CONFIG;