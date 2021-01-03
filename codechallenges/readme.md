# Resources

This django app is used to handle the logic related to code challenge events.

GET CURRENT/QUESTIONS (current) - currently available questions (where current date within questions time range)
GET EXPIRED/QUESTIONS (old) - previosuly available questions
GET QUESTION - get specific question, only if available
GET EVENT - event and associated questions (questions should only be ones actually available)
POST SUBMISSION - create submission for a question, return whether the submission was correct or incorrect