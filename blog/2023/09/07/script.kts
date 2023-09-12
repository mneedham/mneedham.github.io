@file:DependsOn("com.google.code.gson:gson:2.8.6")

import com.google.gson.Gson

data class Person(val name: String)


class Blog {
    companion object {
        @JvmStatic
        fun main(args: Array<String>) {
            println(
                Gson().toJson(Person("Mark Needham"))
            )
        }
    }
}


println("Script started")
println("Before main function call")
Blog.main(arrayOf())
println("After main function call")