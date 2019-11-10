using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class ManagementAnimation : MonoBehaviour {
    Animator animator;

    // Use this for initialization
    void Start () {
		animator = GetComponent<Animator>();		
	}
	
	// Update is called once per frame
	void Update () {
		Angry();
		Terrified();
		Crying();
		Nod();
		Happy();
		Excited();
		Greeting();
		Rejected();
		FeetDance();
		Flip();
	    HipHopWave();
	}

	void Angry(){
		if(Input.GetButtonDown("Key1")){
			animator.SetBool("Angry",true);
		}if(Input.GetButtonUp("Key1")){
			animator.SetBool("Angry",false);
		}
	}

	void Terrified(){
		if(Input.GetButtonDown("Key2")){
			animator.SetBool("Terrified",true);
		}if(Input.GetButtonUp("Key2")){
			animator.SetBool("Terrified",false);
		}
	}

	void Crying(){
		if(Input.GetButtonDown("Key3")){
			animator.SetBool("Crying",true);
		}if(Input.GetButtonUp("Key3")){
			animator.SetBool("Crying",false);
		}
	}

	void Nod(){
		if(Input.GetButtonDown("Key4")){
			animator.SetBool("Nod",true);
		}if(Input.GetButtonUp("Key4")){
			animator.SetBool("Nod",false);
		}
	}

	void Happy(){
		if(Input.GetButtonDown("Key5")){
			animator.SetBool("Happy",true);
		}if(Input.GetButtonUp("Key5")){
			animator.SetBool("Happy",false);
		}
	}

	void Excited(){
		if(Input.GetButtonDown("Key6")){
			animator.SetBool("Excited",true);
		}if(Input.GetButtonUp("Key6")){
			animator.SetBool("Excited",false);
		}
	}

	void Greeting(){
		if(Input.GetButtonDown("Key7")){
			animator.SetBool("Greeting",true);
		}if(Input.GetButtonUp("Key7")){
			animator.SetBool("Greeting",false);
		}
	}

	void Rejected(){
		if(Input.GetButtonDown("Key8")){
			animator.SetBool("Rejected",true);
		}if(Input.GetButtonUp("Key8")){
			animator.SetBool("Rejected",false);
		}
	}

	void FeetDance(){
		if(Input.GetButtonDown("Key9")){
			animator.SetBool("FeetDance",true);
		}if(Input.GetButtonUp("Key9")){
			animator.SetBool("FeetDance",false);
		}
	}

	void Flip(){
		if(Input.GetButtonDown("Key0")){
			animator.SetBool("Flip",true);
		}if(Input.GetButtonUp("Key0")){
			animator.SetBool("Flip",false);
		}
	}

	void HipHopWave(){
		if(Input.GetButtonDown("KeyM")){
			animator.SetBool("HipHopWave",true);
		}if(Input.GetButtonUp("KeyM")){
			animator.SetBool("HipHopWave",false);
		}
	}



	
}
