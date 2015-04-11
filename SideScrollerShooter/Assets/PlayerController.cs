using UnityEngine;
using System.Collections;

public class PlayerController : MonoBehaviour {
	public float speed;

	// Use this for initialization
	void Start () {
	
	}
	
	// Update is called once per frame
	void Update () {
	
	}
	void FixedUpdate(){
		if(Input.GetKey ("w"){
			gameObject.GetComponent<Rigidbody>().AddForce(0.0f, speed, 0.0f);
		}
		if(Input.GetKey ("s"){
			gameObject.GetComponent<Rigidbody>().AddForce(0.0f, -speed, 0.0f);
			
		}
	}
}
