This repository includes a collection of custom ComfyUI nodes designed for highly dynamic prompt generation and structured image output. These nodes work together to enable scalable, automated, and controlled AI image generation, making them ideal for machine learning datasets, concept art, and other AI-driven applications.

## Important Terminology

**Definition** - Think of this as a variable. The ID can be either numerical or named.

**Example:**

ID could be a numerical value from the **Definition AIO Node**:

```javascript
[1, goldfish, alligator, otter]
```

...or it could be named from the **Theme Definition Node(s):**

```javascript
ID: animal
Contents:
goldfish
alligator
otter
```

**Placeholder** - This is how you access the variables you have defined. These would be either numerical or named values.

**Examples:**

```javascript
An old lady petting a [1]
```

```javascript
An old lady petting a [animal]
```

* * *

## Key Features

- **Custom nodes for ComfyUI** – Seamlessly integrate with existing workflows.
- **Up to 50 theme definitions per prompt** – Extreme flexibility for structured generation.
- **Supports multi-pipeline workflows** – Generate thousands of controlled variations from a single Control Prompt node.
- **Exponential variation potential** – With just 5 items per Theme Definition node, this system enables more unique outputs than there are atoms in the observable universe.
- **Dynamic Age Definition node** – Allows precise age-based control over generated images.
- **Optimized for ML and AI training** – Ideal for dataset generation and structured AI art.

* * *

## Who Is This For?

This project is designed for anyone who wants structured, scalable, and dynamic AI image generation. It is especially useful for:

- **AI & ML Researchers** – Create controlled datasets with structured variations for model training.
- **Generative Artists** – Explore a vast range of image outputs without manually tweaking prompts.
- **Game Developers & Concept Designers** – Quickly generate structured variations for characters, environments, and assets.
- **Data Scientists** – Use structured randomness to test AI models in diverse scenarios.
- **Anyone Using ComfyUI for Large-Scale Image Generation** – Automate structured prompt workflows and save time.

* * *

## Installation

To install these custom nodes in your ComfyUI environment, follow these steps:

Navigate to your ComfyUI custom_nodes directory:

```javascript
cd <ComfyUI directory>/custom_nodes
```

Clone this repository:

```javascript
git clone ["URL will be added after publication"]
```

Restart ComfyUI to load the new nodes.

* * *

## Nodes

This package includes several nodes that work together to enable highly dynamic prompt generation:

- **Control Prompt** – Defines the template with placeholders for dynamic replacement.
- **Definition AIO** – Stores and manages dynamic key definitions.
- **Theme Definition** – Allows structured variation by defining different categories of replacement values.
- **Extended Prompt** – Processes the template and dynamically fills in placeholders based on definitions.
- **Theme Combiner** – Merges multiple theme definitions into a single, structured prompt.
- **Age Definition** – Allows controlled variation across age groups.
- **Save Image with Metadata** – Saves generated images with detailed metadata, including prompt information and seed.

* * *

## Node Breakdown

### Control Prompt Node

The **Control Prompt Node** acts as the centralized template for structured, dynamic prompt generation. It allows users to define a single prompt with placeholders, which are later replaced with dynamically selected values from either the **Definition AIO** or **Theme Definition** nodes when sent into the Extended Prompt node. By modifying the Control Prompt, users can instantly alter the structure and content of thousands of generated images without needing to manually adjust individual prompts.

This node ensures that all generated images follow a consistent format while allowing for extensive variation, making it a critical tool for dataset generation, structured AI art, and large-scale prompt automation. If fed into multiple pipelines, each with their own Extended Prompt node, you can change them all by altering just this one input.

Lastly, this node is not necessary. You can use the Extended Prompt node by itself. The benefit of this node is explicitly to allow sending a prompt down-chain from a central controlled location.

**Example Usage**

A user defines the following Control Prompt:

> A \[age\] woman with \[haircolor\] hair in a \[hairstyle\], wearing a \[fabric\], \[clothing-color\] \[clothing\], with \[eye-color\] eyes. She is \[face-direction\] while \[pose\], standing \[location\] with \[lighting\] and \[camera-angle\].

This prompt remains static, but the placeholders are dynamically filled in by the Definition AIO or Theme Definition nodes, enabling a massive range of unique image outputs.

* * *

### Definition AIO Node

The **Definition AIO Node** is designed for storing and managing key definitions as simple arrays, allowing for dynamic placeholder replacement in prompts. Users can define values using numeric placeholders (e.g., \[1\], \[2\]) or named placeholders. This node provides a simple and efficient way to manage large sets of options, though it is not required for structured prompt generation.

Unlike the **Theme Definition Node**, the Definition AIO Node is not instanced—it provides a single dataset that can be referenced across multiple prompts.

The purpose of this node is to make it easier to create variations of like-things, but without tons of nodes to do it (Theme Definition nodes).

**Example Usage**

A user defines the following set of values in the Definition AIO Node:

```javascript
[1, pants, skirt, shorts]  
[2, blonde, brown, black, red]  
[3, smiling, frowning, looking away]  
```

Now, a prompt written as:

> ```
> A person with [2] hair wearing [1], who is [3].
> ```

... could dynamically resolve to:

> ```
> A person with black hair wearing a skirt, who is looking away.
> ```

This node is useful for quickly swapping predefined options without needing to manually configure complex structures.

* * *

### Theme Definition Node

The **Theme Definition Node** is a more advanced and flexible way to define prompt placeholders. Unlike the **Definition AIO Node**, Theme Definition Nodes can be instantiated multiple times, allowing for fine-grained control over different aspects of the prompt. Each instance of this node defines a specific variable (e.g., clothing type, lighting condition, hairstyle), providing greater modularity in structured image generation.

By setting the ID of the variable, you can then reference these with placeholders in your Extended Prompt node.

Additionally, Theme Definition Nodes support entire sentences or detailed descriptions as replacements (or single-word variations), meaning users are not limited to single words or simple subjects.

The Theme Definition Node is fed into the **Theme Combiner Node**, allowing multiple independent definitions to be merged into a single structured dataset. This is great when working with complex, multi-attribute prompts (e.g., combining clothing, environment, and lighting variations) while maintaining controlled randomness across attributes.

**Example Usage**

A user defines a Theme Definition Node for clothing styles:

```javascript
Variable ID: clothing  
Options:  
- A flowing, knee-length sundress with floral patterns  
- A professional, dark-colored suit with a red tie  
- A comfortable, oversized sweater with jeans  
```

Now, a Control Prompt written as:

> ```
> A person is wearing [clothing].
> ```

... could dynamically resolve to:

> ```
> A person is wearing a flowing, knee-length sundress with floral patterns.
> ```

By using multiple Theme Definition Nodes, users can create highly structured prompts that allow for controlled variation across different attributes.

* * *

### Theme Combiner Node

The **Theme Combiner Node** allows users to merge multiple **Theme Definition Nodes** into a single structured dataset, ensuring that all defined themes are accessible within a unified prompt structure. This is useful when working with large-scale image generation where multiple factors (such as building type, lighting, landscape, and background) must be coordinated without manually combining separate lists.

By using the Theme Combiner, users maintain control over structured randomness, ensuring that prompts remain diverse while still adhering to predefined themes.

#### **Example Usage**

- A user defines separate Theme Definition Nodes for clothing, lighting, and background.
- The Theme Combiner merges these definitions into a single dataset.
- The Extended Prompt Node then uses this dataset to generate a coherent and structured output.

This node is essential for users who want organized control over prompt variation without needing to manually synchronize multiple definition sets.

* * *

### Extended Prompt Node

The **Extended Prompt Node** is responsible for processing the **Control Prompt** and dynamically replacing placeholders with values from the **Theme Definitions**, or / and the **Definition AIO**, and optionally the **Age Definition Node**. It assembles the final structured prompt used in image generation, ensuring that placeholders are replaced randomly or systematically based on the definitions provided.

This node also supports seed-based control, meaning it can generate variations of a base prompt while keeping the overall structure intact.

The Extended Prompt Node does not have to use the Control Prompt Node. It can process prompts on its own.

**Example Workflow**

- ```
    The Control Prompt defines a base template with placeholders.
    ```
    
- ```
    The Theme Definition Nodes provide possible values.
    ```
    
- ```
    The Theme Combiner merges structured options.
    ```
    
- ```
    The Extended Prompt Node processes everything and generates the final output.
    ```
    

This node acts as the final stage before prompts are passed into ComfyUI for image generation.

* * *

### Age Definition Node

The **Age Definition Node** allows users to introduce structured age variations within their prompts. Instead of using arbitrary numerical values, this node defines a controlled range of age groups that can be dynamically inserted into prompts. You do not have to use all age slots, nor do they have to be used front to back.

This is particularly useful for dataset generation, concept art, and AI model training, ensuring that generated outputs are not biased toward a single demographic. The Age Definition Node can work alongside other **Theme Definitions** and / or **Definition AIO** to provide greater control over character variation.

**Note: This does not output a numerical value. Instead, if we insert 23, it outputs:**

> 23-year-old

**Example Usage**

A user configures the Age Definition Node with the following values:

```javascript
18, 20, 23, 27, 30, 33, 37, 40, 43, 47, 50, 55
```

A Control Prompt written as:

> ```
> A [age] person is standing in a [location] wearing a [clothing].
> ```

... could dynamically resolve to:

> ```
> A 27-year-old person is standing in a garden wearing a dark-colored suit with a red tie.
> ```

By controlling age variation systematically, this node helps in balancing datasets for AI research.

* * *

### Save Image with Metadata Node

This node is designed to save generated images while embedding metadata, ensuring that prompts and seeds are retained within the file. This is particularly useful for researchers, dataset curators, and artists who need to track the specifics of their image outputs.

This node can also be output as an image to Preview Image nodes or other workflow needs.

**Key features include:**

- ```
    Saves prompt text within EXIF metadata, allowing for easy retrieval.
    ```
    
- ```
    Includes the seed value in the filename (formatted as seed-xxxxx.jpg).
    ```
    
- ```
    Ensures lossless storage of prompt information, making it easy to reproduce previous generations.
    ```
    

**Example Workflow**

- ```
    The Extended Prompt Node generates a structured prompt.
    ```
    
- ```
    An AI image generation pipeline produces an image.
    ```
    
- ```
    The Save Image with Metadata Node stores the image with all relevant details embedded.
    ```
    

This ensures that every image remains traceable, reproducible, and well-documented.

* * *