# Interview Questions

# Amagi

## **Minimum time required to complete all tasks with alteration of their order allowed**

[Task Scheduler - LeetCode](https://leetcode.com/problems/task-scheduler/)

Given a string S consisting of N characters (representing the tasks to perform) and a positive integer K, the task is to find the minimum time required to complete all the given tasks in any order, given that each task takes one unit of time and each task of the same type must be performed at an interval of K units.

Examples:

```
Input: S = "AAABBB", K = 2
Output: 8
Explanation:
Below are the order of task that is to be completed:
A → B → _ → A → B → _ → A → B
Therefore, the total time required is 8 units.

Input: S = “AAABBB”, K = 0
Output: 6
```

### **Solution:**

```java
class Solution {
    public int leastInterval(char[] tasks, int n) {
        int[] freq = new int[26];
        for(char c: tasks) {
            freq[c-'A']++;
        }
        Arrays.sort(freq);
				// Once we arrange the task with highest frequency, 
				// spaces will be the total number of empty space between those tasks.
        int spaces = (freq[25]-1)*n;

        for(int i=24;i>=0;i--) {
						// task with same as maximum frequency task will use frequency-1 space
            spaces = spaces - ((freq[i]==freq[25])?freq[i]-1:freq[i]);
        }
				// If spaces are remaining then add it to the total task 
				// otherwise there is no idle time (empty space)
        spaces = Math.max(spaces, 0);
        return tasks.length+spaces;
    }
}
```

## **Elevator design**

## **Check if a given Binary Tree is SumTree**

### Solution

```sql
#include <iostream>
using namespace std;

class Node {
	public:
		int value;
		Node* left;
		Node* right;
	
	public:
		Node(int v) {
			value = v;
			left = NULL;
			right = NULL;
		}
};

bool checkSumTree(Node *n) {
	bool myD=false, leftD=false, rightD=false;
	if(n->left==NULL && n->right==NULL) {
		return true;
	}
	if(n->left!=NULL && n->right!=NULL) {
		if(n->value == n->left->value + n->right->value) {
			myD = true;
		} else {
			myD = false;
			return false;
		}
		leftD = checkSumTree(n->left);
		rightD = checkSumTree(n->right);
	}
	return leftD && rightD;
}

int main() {
	Node *root = new Node(10);
	Node *dleft = new Node(6);
	Node *ddleft = new Node(3);
	Node *ddright = new Node(3);
	Node *dright = new Node(4);
	// Node *rlright = new Node(2);
	// Node *rlleft = new Node(2);
	root->left = dleft;
	root->right = dright;
	root->left->left = ddleft;
	root->left->right = ddright;
	// root->right->left = rlleft;
	// root->right->right = rlright;
	if(checkSumTree(root)){
		cout<<"YES"<<endl;	
	} else {
		cout<<"NO"<<endl;	
	}
	return 0;
}
```

## Design tv channel recommendation

Requirement:

Build a pipeline to ingest data for video recommendation system.

```
User Profile
-> Trending categories (all user space)
	- categories sorted by trend, latest
-> Personalise categories
	- (lastest, most)
	- build on users's history

Video is being (video hearbeat)
(event) -> (user_id, content_id, event_timestamp, video_play_timestamp)
-> kafka, redddis
-> Consumer -> kafka connect
-> cloud storage (s3), (JSON)
-> Athena, Hive queries

fast computation, data size reduction
ORC, PARQUE

- Hourly aggregation
- Daily aggregation

hourly_raw_event
select 
	user_id, 
	content_id,
	max(event_timestamp) as latest_timestamp,
	max(video_play_timestamp) max_video_timestamp,
	min(video_play_timestamp) min_video_timestamp,
	(max(video_play_timestamp)-min(video_play_timestamp)) video_duration = t2-t1
group by user_id, content_id

=> put into s3 (warehouse)

=> content metadata table
content_id, categories, duration
=> genre, sub genre
unique(content_id, category)

user_id,
genre,
video_percentage => min_video_timestamp -> video_start_time
video_duration/(content_duration-video_start_time(5th minute))

t0

t1
t2

t10

(t2-t1)/(t10-t1) 

Video Metadata
content_id -> metadata (genres)

VideoLibrary (userProfile)

video -> categories

avg_vedio_percentage =>

category => percentage (100)

latest trend of user => simple average with existing category and latest percentage

Two more attribute that is very important in designing recommendation system is time attribute. 
1. Hour of the day
Because user's interest varies over hour of dat. To explain this, let's take a example of family with kid. It is more likely that kis dominates the day and parent dominate the night time. Meaning if while building profile if we add hour of the dat as one more attribute then recommendation will be improved. It is more likely to assume that News, Movie, TV serial genres are dominent in evening/night time compare to day time. Cartoon genre is more watched during day time as kids dominent the TV during day.

2. Day of the week (week day, weekend)
Second attribute that is equally important as hour of time is DAY of the week. It is reasonable to build different profile for week day and weekend. As user's livelihood is different during weekdays and weekend. So it also important to take account of this attribute as well to build good recommendation system.
```