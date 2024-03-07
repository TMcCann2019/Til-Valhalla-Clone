Welcome to Til Valhalla (clone of Til Valhalla Project)

BASIC LAYOUT OF HOW THE SITE WILL WORK:  
Within this website, you (the user) will have access to the following:
1. See the home page with information about the project and the site itself
2. See all of our products that are available
   * From this page, you will be able to filter the different products to find the ones you want (coming in later versions of the site)
   * You can also leave reviews on items you have bought or tried (star rating)(coming in later versions of the site)
3. Signin to your account if you have one or signup a new account
4. Ability to create a new product with a name, description, image, price, size and color

BREAKDOWN OF THE PRODUCT PAGE:  
As a user on the prodcut page, you can do the following:
1. Update aspects of the product (description, price, size, color)
2. Delete a product 
3. Add to a cart feature

BREAKDOWN OF SIGNUP/SINGIN PAGE:    
1. Usage  
To use the Authentication component:  
Import the Component: Import the Authentication component into your React application.
  
Pass Props: Ensure to pass the updateUser function as a prop to the Authentication component. This function should be responsible for updating the user state upon successful authentication.
  
Integrate with Routing: Ensure that the Authentication component is rendered within the appropriate route of your application, typically where user authentication is required.
  
Customization: Customize the component's appearance and behavior according to your application's requirements.
  
2. Code Overview  
The Authentication component is structured as follows:  
  
State Management: Utilizes the useState hook to manage the state for signup mode.
  
Form Handling: Utilizes Formik and Yup for form validation and submission. Dynamically validates the email field based on the signup mode.
  
Routing: Uses the useHistory hook from React Router to navigate users upon successful authentication.
  
User Feedback: Provides feedback to users by displaying validation errors and prompts to log in or sign up based on the current mode.
  
3. Dependencies  
The Authentication component relies on the following dependencies:  
  
React  
React Router  
Formik  
Yup  
Ensure these dependencies are installed in your project for the component to work correctly.  
  
4. Props  
The Authentication component expects the following prop:  
  
updateUser: Function to update the user state upon successful authentication.