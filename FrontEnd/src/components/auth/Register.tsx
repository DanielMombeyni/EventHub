/* eslint-disable @typescript-eslint/no-unused-vars */
import { Formik, Form, Field, ErrorMessage } from "formik";
import * as Yup from "yup";

const RegisterForm = () => {
  const initialValues = {
    username: "",
    email: "",
    password: "",
    confirmPassword: "",
  };

  const validationSchema = Yup.object({
    username: Yup.string().required("Username is required"),
    email: Yup.string()
      .email("Invalid email address")
      .required("Email is required"),
    password: Yup.string()
      .min(8, "Password must be at least 8 characters long")
      .required("Password is required"),
    confirmPassword: Yup.string()
      .oneOf([Yup.ref("password"), null], "Passwords must match")
      .required("Confirm Password is required"),
  });

  const onSubmit = (values: unknown, { setSubmitting }: unknown) => {
    console.log("Form data", values);
    setSubmitting(false);
  };

  return (
    <div className="max-w-md mx-auto">
      <h1 className="text-2xl font-bold mb-4">Register</h1>
    </div>
  );
};

export default RegisterForm;
